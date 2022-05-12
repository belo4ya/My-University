from functools import lru_cache
import numpy as np


def transition_probability(matrix, k):
    """Вероятность перехода из x в y за k шагов"""
    return np.linalg.matrix_power(matrix, k)


def state_probability(matrix, start, k):
    """Вероятность состояния за k шагов"""
    return start.dot(np.linalg.matrix_power(matrix, k))


def first_transition_probability(matrix, k):
    """Вероятность первого перехода за k шагов"""
    prev = np.copy(matrix)
    for _ in range(k - 1):
        prev = matrix_power_with_skip(matrix, prev)

    return prev


def last_transition_probability(matrix, k):
    """Вероятность перехода не позднее чем за k шагов"""
    prev, res = np.copy(matrix), np.copy(matrix)
    for t in range(k - 1):
        prev = matrix_power_with_skip(matrix, prev)
        res += prev

    return res


def avg_steps(matrix):
    """Среднее количество шагов, необходимых для первого перехода"""
    prev, res = np.copy(matrix), np.copy(matrix)
    for t in range(993):
        prev = matrix_power_with_skip(matrix, prev)
        res += t * prev

    return res


def first_return_probability(matrix, k):
    """Вероятность первого возвращения на k-ом шаге"""
    _matrix = np.copy(matrix)
    p_jj = transition_probability

    @lru_cache(maxsize=None)
    def f_jj(_k):
        return p_jj(_matrix, _k) - sum([f_jj(m) * p_jj(_matrix, _k - m) for m in range(1, _k)])

    return np.diagonal(f_jj(k))


def avg_time_return(matrix):
    """Среднее время возвращения"""
    _matrix = np.copy(matrix)
    p_jj = transition_probability
    result = []

    @lru_cache(maxsize=None)
    def f_jj(_k):
        res = p_jj(_matrix, _k) - sum([f_jj(m) * p_jj(_matrix, _k - m) for m in range(1, _k)])
        result.append(_k * np.diagonal(res))
        return res

    f_jj(993)
    return sum(result)


def last_return_probability(matrix, k):
    """Вероятность возвращения не позднее чем за k шагов"""
    _matrix = np.copy(matrix)
    p_jj = transition_probability
    result = []

    @lru_cache(maxsize=None)
    def f_jj(_k):
        res = p_jj(_matrix, _k) - sum([f_jj(m) * p_jj(_matrix, _k - m) for m in range(1, _k)])
        result.append(np.diagonal(res))
        return res

    f_jj(k)
    return sum(result)


def steady_state_probabilities(matrix):
    """Установившиеся вероятности"""
    matrix_ = np.copy(matrix).transpose()
    np.fill_diagonal(matrix_, np.diagonal(matrix_) - 1)
    matrix_[-1, :] = 1

    vec_b = np.zeros(len(matrix_))
    vec_b[-1] = 1
    return np.linalg.inv(matrix_).dot(vec_b)


def matrix_power_with_skip(left, right):
    range_ = range(len(left))
    return np.array([[sum(left[i, m] * right[m, j] if m != j else 0 for m in range_) for j in range_] for i in range_])


def validate(matrix):
    assert matrix.shape == (13, 13), "Размер матрицы должен быть (13, 13)"
    assert np.equal(np.sum(matrix, axis=1), np.matrix(np.ones(13))).all(), (
        "Сумма вероятностей в каждой строке должна равняться 1"
    )
    assert (np.count_nonzero(transition_matrix, axis=1) ==
            np.array([3, 3, 3, 3, 1, 2, 4, 5, 2, 2, 4, 3, 1]) + 1).all(), (
        "Количество исходящих вероятностей должно быть [3, 3, 3, 3, 1, 2, 4, 5, 2, 2, 4, 3, 1]"
    )


def answer(res):
    return f"Ответ: {res}\n"


if __name__ == '__main__':
    transition_matrix = np.array([
        [0.09, 0.56, 0, 0, 0.34, 0.01, 0, 0, 0, 0, 0, 0, 0],
        [0.47, 0.3, 0, 0.18, 0.05, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0.31, 0.11, 0, 0.33, 0.25, 0, 0, 0, 0, 0, 0, 0],
        [0.24, 0.2, 0, 0.31, 0, 0, 0.25, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0.39, 0.61, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.23, 0, 0.49, 0.28, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0.34, 0.24, 0, 0.04, 0, 0, 0, 0.35, 0.03, 0],
        [0, 0, 0, 0, 0.26, 0, 0.2, 0.22, 0.28, 0.02, 0.02, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0.07, 0.61, 0.32, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0.69, 0, 0.24, 0.07, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0.3, 0, 0, 0.31, 0.03, 0.13, 0.23],
        [0, 0, 0, 0, 0, 0, 0.59, 0.05, 0, 0, 0.29, 0.07, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.87, 0, 0, 0.13]
    ])
    validate(transition_matrix)

    print("Матрица переходов:")
    print(transition_matrix, "\n")

    # 1
    k, i, j = 10, 10, 1
    transition = transition_probability(transition_matrix, k)
    print(f"1. вероятность того, что за {k} шагов система перейдет из состояния {i} в состояние {j}:")
    print(answer(transition[i - 1, j - 1]))

    # 2
    k = 10
    a_0 = np.array([0, 0.03, 0.08, 0.14, 0.16, 0.04, 0.13, 0.11, 0.07, 0.11, 0.01, 0.06, 0.06])
    state = state_probability(transition_matrix, a_0, k)
    print(f"2. вероятности состояний системы спустя {k} шагов, если в начальный "
          f"момент вероятность состояний были следующими A={a_0}:")
    print(answer(state))

    # 3
    k, i, j = 9, 11, 5
    first_transition = first_transition_probability(transition_matrix, k)
    print(f"3. вероятность первого перехода за {k} шагов из состояния {i} в состояние {j}:")
    print(answer(first_transition[i - 1, j - 1]))

    # 4
    k, i, j = 6, 6, 3
    last_transition = last_transition_probability(transition_matrix, k)
    print(f"4. вероятность перехода из состояния {i} в состояние {j} не позднее чем за {k} шагов:")
    print(answer(last_transition[i - 1, j - 1]))

    # 5
    i, j = 7, 10
    avg_steps_number = avg_steps(transition_matrix)
    print(f"5. среднее количество шагов для перехода из состояния {i} в состояние {j}:")
    print(answer(avg_steps_number[i - 1, j - 1]))

    # 6
    k, i = 7, 9
    first_return = first_return_probability(transition_matrix, k)
    print(f"6. вероятность первого возвращения в состояние {i} за {k} шагов:")
    print(answer(first_return[i - 1]))

    # 7
    k, i = 8, 12
    last_return = last_return_probability(transition_matrix, k)
    print(f"7. вероятность возвращения в состояние {i} не позднее чем за {k} шагов")
    print(answer(last_return[i - 1]))

    # 8
    i = 7
    avg_time_to_return = avg_time_return(transition_matrix)
    print(f"8. среднее время возвращения в состояние {i}")
    print(answer(avg_time_to_return[i - 1]))

    # 9
    steady_state = steady_state_probabilities(transition_matrix)
    print("9. установившиеся вероятности:")
    print(answer(steady_state))

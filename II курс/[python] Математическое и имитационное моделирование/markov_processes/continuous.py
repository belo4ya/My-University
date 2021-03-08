import numpy as np


def steady_state_probability(matrix):
    """Установившиеся вероятности"""
    size = len(matrix)
    matrix_ = np.copy(matrix).transpose()
    np.fill_diagonal(matrix_, [-sum(matrix_[:, i]) for i in range(size)])
    matrix_[-1, :] = 1

    vec_b = np.zeros(size)
    vec_b[-1] = 1
    return np.linalg.inv(matrix_).dot(vec_b)


def failure_probability(s_state):
    """Вероятность отказа"""
    return s_state[-1]


def relative_and_absolute_service_intensity(s_state, la):
    """Относительная и абсолютная интенсивность обслуживания"""
    relative = 1 - s_state[-1]
    return relative, relative * la


def average_queue_length(s_state, m, n):
    """Средняя длина очереди"""
    return sum((i * s_state[m + i]) for i in range(1, n + 1))


def average_queue_time(s_state, m, n, mu):
    """Среднее время в очереди"""
    return sum(((i + 1) / (m * mu) * s_state[m + i]) for i in range(n))


def average_number_busy_channels(s_state, m, n):
    """Среднее число занятых каналов"""
    return (sum((i * s_state[i]) for i in range(1, m + 1)) +
            sum((m * s_state[i]) for i in range(m + 1, m + n + 1)))


def skip_queue_probability(s_state, m):
    """Вероятность не ждать в очереди"""
    return sum(s_state[:m])


def average_downtime(matrix):
    """Среднее время простоя системы массового обслуживания"""
    return 1 / np.sum(matrix, axis=1)


def init_matrix(n, m, la, mu):
    size = n + m + 1
    matrix = np.zeros((size, size))
    np.fill_diagonal(matrix[:, 1:], la)
    np.fill_diagonal(matrix[1:, :], [*[i * mu for i in range(1, m)], *[m * mu for _ in range(n + 1)]])
    return matrix


def validate(matrix):
    size = n + m + 1
    assert matrix.shape == (size, size), f"Размер матрицы должен быть {size}"


def answer(*args):
    res = ", ".join([str(i) for i in args])
    return f"Ответ: {res}\n"


if __name__ == '__main__':
    la = 32
    m = 5
    mu = 8
    n = 17
    initial_matrix = init_matrix(n, m, la, mu)
    validate(initial_matrix)

    # a
    steady_state = steady_state_probability(initial_matrix)
    print("a) Составьте граф марковского процесса, запишите систему уравнений Колмогорова и "
          "найдите установившиеся вероятности состояний:")
    print(answer(steady_state))

    # b
    fail_probability = failure_probability(steady_state)
    print("b) Найдите вероятность отказа в обслуживании:")
    print(answer(fail_probability))

    # c
    relative, absolute = relative_and_absolute_service_intensity(steady_state, la)
    print("c) Найдите относительную и абсолютную интенсивность обслуживания:")
    print(answer(relative, absolute))

    # d
    avg_queue_len = average_queue_length(steady_state, m, n)
    print("d) Найдите среднюю длину в очереди:")
    print(answer(avg_queue_len))

    # e
    avg_queue_time = average_queue_time(steady_state, m, n, mu)
    print("e) Найдите среднее время в очереди:")
    print(answer(avg_queue_time))

    # f
    avg_number_channels = average_number_busy_channels(steady_state, m, n)
    print("f) Найдите среднее число занятых каналов:")
    print(answer(avg_number_channels))

    # g
    skip_probability = skip_queue_probability(steady_state, m)
    print("g) Найдите вероятность того, что поступающая заявка не будет ждать в очереди:")
    print(answer(skip_probability))

    # h
    avg_downtime = average_downtime(initial_matrix)
    print("h) Найти среднее время простоя системы массового обслуживания:")
    print(answer(avg_downtime[0]))

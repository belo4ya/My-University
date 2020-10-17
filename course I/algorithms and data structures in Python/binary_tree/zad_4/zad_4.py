from timetest import time_test
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation
import time
import sys
sys.path.insert(0, '../')
from binary_tree import BinaryTree


def draw_tree(label, node='line', color='#000'):
    prm = {
        'x': 0,
        'y': 0,
        'size': 1500,
        'font-size': 18,
        'align': 'center',
        'colors': {
            'line': '#000',
            10: '#dbd7d2',
            12: '#dbd7d2',
            13: '#dbd7d2',
            15: '#dbd7d2',
            20: '#dbd7d2',
            24: '#dbd7d2',
            27: '#dbd7d2',
            33: '#dbd7d2',
            42: '#dbd7d2',
            51: '#dbd7d2',
            57: '#dbd7d2',
            68: '#dbd7d2',
            77: '#dbd7d2',
            79: '#dbd7d2',
            81: '#dbd7d2',
            'A': '#cee6ad',
            'B': '#fbcea9',
            'C': '#fbcea9',
            'D': '#d6c5de',
            'E': '#d6c5de',
            'F': '#d6c5de',
            'G': '#adc5de',
            'H': '#adc5de',
            'I': '#adc5de',
        }
    }
    tmp = prm['colors'][node]
    prm['colors'][node] = color

    # 10
    ax.add_line(Line2D([prm['x'] + 0.5, prm['x']], [prm['y'] + 1, prm['y'] + 0],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'], prm['y'], prm['size'], color=prm['colors'][10])
    ax.text(prm['x'], prm['y'], '10', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 13
    ax.add_line(Line2D([prm['x'] + 0.5, prm['x'] + 1], [prm['y'] + 1, prm['y'] + 0],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'] + 1, prm['y'], prm['size'], color=prm['colors'][13])
    ax.text(prm['x'] + 1, prm['y'], '13', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 20
    ax.add_line(Line2D([prm['x'] + 2.5, prm['x'] + 2], [prm['y'] + 1, prm['y'] + 0],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'] + 2, prm['y'], prm['size'], color=prm['colors'][20])
    ax.text(prm['x'] + 2, prm['y'], '20', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 27
    ax.add_line(Line2D([prm['x'] + 2.5, prm['x'] + 3], [prm['y'] + 1, prm['y'] + 0],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'] + 3, prm['y'], prm['size'], color=prm['colors'][27])
    ax.text(prm['x'] + 3, prm['y'], '27', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 42
    ax.add_line(Line2D([prm['x'] + 4.5, prm['x'] + 4], [prm['y'] + 1, prm['y'] + 0],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'] + 4, prm['y'], prm['size'], color=prm['colors'][42])
    ax.text(prm['x'] + 4, prm['y'], '42', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 57
    ax.add_line(Line2D([prm['x'] + 4.5, prm['x'] + 5], [prm['y'] + 1, prm['y'] + 0],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'] + 5, prm['y'], prm['size'], color=prm['colors'][57])
    ax.text(prm['x'] + 5, prm['y'], '57', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 77
    ax.add_line(Line2D([prm['x'] + 6.5, prm['x'] + 6], [prm['y'] + 1, prm['y'] + 0],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'] + 6, prm['y'], prm['size'], color=prm['colors'][77])
    ax.text(prm['x'] + 6, prm['y'], '77', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 81
    ax.add_line(Line2D([prm['x'] + 6.5, prm['x'] + 7], [prm['y'] + 1, prm['y'] + 0],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'] + 7, prm['y'], prm['size'], color=prm['colors'][81])
    ax.text(prm['x'] + 7, prm['y'], '81', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 12
    ax.add_line(Line2D([prm['x'] + 1.5, prm['x'] + 0.5], [prm['y'] + 2, prm['y'] + 1],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'] + 0.5, prm['y'] + 1, prm['size'], color=prm['colors'][12])
    ax.text(prm['x'] + 0.5, prm['y'] + 1, '12', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 24
    ax.add_line(Line2D([prm['x'] + 1.5, prm['x'] + 2.5], [prm['y'] + 2, prm['y'] + 1],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'] + 2.5, prm['y'] + 1, prm['size'], color=prm['colors'][24])
    ax.text(prm['x'] + 2.5, prm['y'] + 1, '24', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 51
    ax.add_line(Line2D([prm['x'] + 5.5, prm['x'] + 4.5], [prm['y'] + 2, prm['y'] + 1],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'] + 4.5, prm['y'] + 1, prm['size'], color=prm['colors'][51])
    ax.text(prm['x'] + 4.5, prm['y'] + 1, '51', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 79
    ax.add_line(Line2D([prm['x'] + 5.5, prm['x'] + 6.5], [prm['y'] + 2, prm['y'] + 1],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'] + 6.5, prm['y'] + 1, prm['size'], color=prm['colors'][79])
    ax.text(prm['x'] + 6.5, prm['y'] + 1, '79', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 15
    ax.add_line(Line2D([prm['x'] + 3.5, prm['x'] + 1.5], [prm['y'] + 3, prm['y'] + 2],
                       color=prm['colors']['line']))
    ax.scatter(prm['x'] + 1.5, prm['y'] + 2, prm['size'], color=prm['colors'][15])
    ax.text(prm['x'] + 1.5, prm['y'] + 2, '15', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 68
    ax.add_line(Line2D([prm['x'] + 3.5, prm['x'] + 5.5], [prm['y'] + 3, prm['y'] + 2],
                       color=prm['colors']['line'], label=label))
    ax.scatter(prm['x'] + 5.5, prm['y'] + 2, prm['size'], color=prm['colors'][68])
    ax.text(prm['x'] + 5.5, prm['y'] + 2, '68', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])
    # 33
    ax.scatter(prm['x'] + 3.5, prm['y'] + 3, prm['size'], color=prm['colors'][33])
    ax.text(prm['x'] + 3.5, prm['y'] + 3, '33', verticalalignment=prm['align'],
            horizontalalignment=prm['align'], fontsize=prm['font-size'])

    [line.set_zorder(0) for line in ax.lines]
    ax.legend(prop={'size': 14}, loc=2)
    prm['colors'][node] = tmp


def animate(i):
    ax.clear()
    ax.grid()
    ax.set_xlim((-1, 8))
    ax.set_ylim((-1, 4))
    ax.set_aspect("equal")
    if i >= len(stack[1]) - 1:
        draw_tree(stack[1][len(stack[1])-1], stack[1][len(stack[1])-1], '#ff9466')
    else:
        draw_tree(stack[1][i], stack[1][i], '#61ffc2')


@time_test
def py_search(arr, el):
    try:
        return arr[arr.index(el)]
    except ValueError:
        return None


@time_test
def tree_search(tree, el):
    return tree.find(tree, el)


@time_test
def tree_iter_search(tree, el):
    return tree.iter_find(el)


if __name__ == '__main__':
    ARR = [81, 77, 79, 68, 10, 12, 13, 20, 15, 24, 27, 42, 33, 51, 57]
    sort_arr = sorted(ARR)
    while True:
        elem = None
        try:
            elem = int(input('>>> '))
        except ValueError:
            print('Введите целое число')
        if elem in ARR:
            break
        else:
            print('Введите число, которое находится в массиве:')
            print(ARR)
            print('Это нужно для корректной отрисовки, не для поиска')
    # Представление в виде дерева
    tree = BinaryTree().create_by_sort_arr(ARR)
    print('Дерево:')
    print(tree)
    # Поиск в массиве
    print('\nПоиск в массиве')
    print('Элемент `' + str(py_search(ARR, elem)) + '` найден!')
    # Поиск в отсортированном массиве
    print('\nПоиск в отсортированном массиве')
    print('Элемент `' + str(py_search(sort_arr, elem)) + '` найден!')
    # Поиск в сбалансированном дереве
    print('\nПоиск в сбалансированном дереве (рекурсивный)')
    print('Элемент `' + str(tree_search(tree, elem).value) + '` найден!')
    print('\nПоиск в сбалансированном дереве (итеративный)')
    print('Элемент `' + str(tree_iter_search(tree, elem)[0].value) + '` найден!')
    # Сравнительный анализ
    print('\nСравнительный анализ:')
    print('\n|' + '-' * 90 + '|\n')
    print(
"""
     Самым эффективным оказался стандартный поиск Python, представленный
  (скоре всего, по тестам выходит так) линейным поиском, который,
  в худшем случае, выполняется за O(n). - ~ 0.0000006 s
     На отсортированном массиве Бинарный поиск был бы эффективнее (O(log n)).
  При этом мы не учитывем время на сортировку массива ~ O(n log n).
     Поиск в сбалансированном бинарном дереве (учитывая, что структура данных
  реализована на Python, в отличии от list и .index()) дал очень хороший
  результат ~ 0.0000012 s (O(log n)). Но мы не учитывали время на создание
  сбалансированного дерева - O(n * log n) из отсортированного массива (O(n log n)).
     Таким образом, можно сделать вывод, что использование бинарных деревьев
  для представления даннх и последующего поиска в них является достатоно эффективным.
"""
    )
    print('\n|' + '-' * 90 + '|\n')
    # Отрисовка дерева и анимация
    stack = tree.iter_find(elem)
    fig, ax = plt.subplots(figsize=(14, 14), dpi=100)
    print('>>> loading...')
    anim = FuncAnimation(fig, animate, interval=500, frames=len(stack[1]) + 4)
    anim.save(f'zad_4_{elem}.gif', writer='imagemagick')
    print('>>> Done')
    plt.show()

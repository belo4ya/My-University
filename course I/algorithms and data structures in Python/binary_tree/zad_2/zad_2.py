import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import sys
sys.path.insert(0, '../')
from binary_tree import BinaryTree


def graph_1():
    x = 7
    y = 2
    size = 550
    fontsize = 10
    # left 2
    axes[0].add_line(Line2D([x, x + 1], [y, y + 2], color='#696969', label=result[0]))
    axes[0].scatter(x, y, size, color='pink')
    axes[0].text(x, y, '2', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # right 2
    axes[0].add_line(Line2D([x + 2, x + 1], [y, y + 2], color='#696969'))
    axes[0].scatter(x + 2, y, size, color='pink')
    axes[0].text(x + 2, y, '2', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # +
    axes[0].scatter(x + 1, y + 2, size, color='#87cefa')
    axes[0].text(x + 1, y + 2, '+', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)

    [line.set_zorder(0) for line in axes[0].lines]
    axes[0].legend(prop={'size': 8.5}, loc=2)


def graph_2():
    x = 5.5
    y = 1
    size = 550
    fontsize = 10
    # left 2
    axes[1].add_line(Line2D([x, x + 1], [y, y + 2], color='#696969', label=result[1]))
    axes[1].scatter(x, y, size, color='pink')
    axes[1].text(x, y, '2', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # right 3
    axes[1].add_line(Line2D([x + 2, x + 1], [y, y + 2], color='#696969'))
    axes[1].scatter(x + 2, y, size, color='pink')
    axes[1].text(x + 2, y, '3', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # +
    axes[1].add_line(Line2D([x + 1, x + 2.5], [y + 2, y + 4], color='#696969'))
    axes[1].scatter(x + 1, y + 2, size, color='#87cefa')
    axes[1].text(x + 1, y + 2, '+', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 4
    axes[1].add_line(Line2D([x + 4, x + 2.5], [y + 2, y + 4], color='#696969'))
    axes[1].scatter(x + 4, y + 2, size, color='pink')
    axes[1].text(x + 4, y + 2, '4', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # *
    axes[1].scatter(x + 2.5, y + 4, size, color='#87cefa')
    axes[1].text(x + +2.5, y + 4, '*', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)

    [line.set_zorder(0) for line in axes[1].lines]
    axes[1].legend(prop={'size': 8.5}, loc=2)


def graph_3():
    x = 5
    y = 1
    size = 550
    fontsize = 10
    # 7
    axes[2].add_line(Line2D([x, x + 1], [y, y + 2], color='#696969', label=result[2]))
    axes[2].scatter(x, y, size, color='pink')
    axes[2].text(x, y, '7', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 8
    axes[2].add_line(Line2D([x + 2, x + 1], [y, y + 2], color='#696969'))
    axes[2].scatter(x + 2, y, size, color='pink')
    axes[2].text(x + 2, y, '8', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # +
    axes[2].add_line(Line2D([x + 1, x + 3], [y + 2, y + 4], color='#696969'))
    axes[2].scatter(x + 1, y + 2, size, color='#87cefa')
    axes[2].text(x + 1, y + 2, '+', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 1
    axes[2].add_line(Line2D([x + 6, x + 5], [y, y + 2], color='#696969'))
    axes[2].scatter(x + 6, y, size, color='pink')
    axes[2].text(x + 6, y, '1', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 2
    axes[2].add_line(Line2D([x + 4, x + 5], [y, y + 2], color='#696969'))
    axes[2].scatter(x + 4, y, size, color='pink')
    axes[2].text(x + 4, y, '2', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # -
    axes[2].add_line(Line2D([x + 5, x + 3], [y + 2, y + 4], color='#696969'))
    axes[2].scatter(x + 5, y + 2, size, color='#87cefa')
    axes[2].text(x + 5, y + 2, '-', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # *
    axes[2].scatter(x + 3, y + 4, size, color='#87cefa')
    axes[2].text(x + 3, y + 4, '*', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)

    [line.set_zorder(0) for line in axes[2].lines]
    axes[2].legend(prop={'size': 8.5}, loc=2)


def graph_4():
    x = 2
    y = 0
    size = 550
    fontsize = 10
    # 7
    axes[3].add_line(Line2D([x, x + 1], [y, y + 2], color='#696969', label=result[3]))
    axes[3].scatter(x, y, size, color='pink')
    axes[3].text(x, y, '7', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 8
    axes[3].add_line(Line2D([x + 2, x + 1], [y, y + 2], color='#696969'))
    axes[3].scatter(x + 2, y, size, color='pink')
    axes[3].text(x + 2, y, '8', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # +
    axes[3].add_line(Line2D([x + 1, x + 3], [y + 2, y + 4], color='#696969'))
    axes[3].scatter(x + 1, y + 2, size, color='#87cefa')
    axes[3].text(x + 1, y + 2, '+', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 1
    axes[3].add_line(Line2D([x + 6, x + 5], [y, y + 2], color='#696969'))
    axes[3].scatter(x + 6, y, size, color='pink')
    axes[3].text(x + 6, y, '1', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 2
    axes[3].add_line(Line2D([x + 4, x + 5], [y, y + 2], color='#696969'))
    axes[3].scatter(x + 4, y, size, color='pink')
    axes[3].text(x + 4, y, '2', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # -
    axes[3].add_line(Line2D([x + 5, x + 3], [y + 2, y + 4], color='#696969'))
    axes[3].scatter(x + 5, y + 2, size, color='#87cefa')
    axes[3].text(x + 5, y + 2, '-', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # *
    axes[3].add_line(Line2D([x + 3, x + 6], [y + 4, y + 6], color='#696969'))
    axes[3].scatter(x + 3, y + 4, size, color='#87cefa')
    axes[3].text(x + 3, y + 4, '*', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 7
    axes[3].add_line(Line2D([x + 9, x + 6], [y + 4, y + 6], color='#696969'))
    axes[3].scatter(x + 9, y + 4, size, color='pink')
    axes[3].text(x + 9, y + 4, '7', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # +
    axes[3].scatter(x + 6, y + 6, size, color='#87cefa')
    axes[3].text(x + 6, y + 6, '+', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)

    [line.set_zorder(0) for line in axes[3].lines]
    axes[3].legend(prop={'size': 8.5}, loc=2)


def graph_5():
    x = 1
    y = 0
    size = 550
    fontsize = 10
    # 7
    axes[4].add_line(Line2D([x, x + 1], [y, y + 2], color='#696969', label=result[4]))
    axes[4].scatter(x, y, size, color='pink')
    axes[4].text(x, y, '7', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 8
    axes[4].add_line(Line2D([x + 2, x + 1], [y, y + 2], color='#696969'))
    axes[4].scatter(x + 2, y, size, color='pink')
    axes[4].text(x + 2, y, '8', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # +
    axes[4].add_line(Line2D([x + 1, x + 3], [y + 2, y + 4], color='#696969'))
    axes[4].scatter(x + 1, y + 2, size, color='#87cefa')
    axes[4].text(x + 1, y + 2, '+', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 2
    axes[4].add_line(Line2D([x + 6, x + 5], [y, y + 2], color='#696969'))
    axes[4].scatter(x + 6, y, size, color='pink')
    axes[4].text(x + 6, y, '2', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 5
    axes[4].add_line(Line2D([x + 4, x + 5], [y, y + 2], color='#696969'))
    axes[4].scatter(x + 4, y, size, color='pink')
    axes[4].text(x + 4, y, '5', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # /
    axes[4].add_line(Line2D([x + 5, x + 3], [y + 2, y + 4], color='#696969'))
    axes[4].scatter(x + 5, y + 2, size, color='#87cefa')
    axes[4].text(x + 5, y + 2, '-', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # *
    axes[4].add_line(Line2D([x + 3, x + 7], [y + 4, y + 6], color='#696969'))
    axes[4].scatter(x + 3, y + 4, size, color='#87cefa')
    axes[4].text(x + 3, y + 4, '*', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # -
    axes[4].add_line(Line2D([x + 11, x + 7], [y + 4, y + 6], color='#696969'))
    axes[4].scatter(x + 11, y + 4, size, color='#87cefa')
    axes[4].text(x + 11, y + 4, '-', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 2
    axes[4].add_line(Line2D([x + 9, x + 11], [y + 2, y + 4], color='#696969'))
    axes[4].scatter(x + 9, y + 2, size, color='pink')
    axes[4].text(x + 9, y + 2, '2', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # 1
    axes[4].add_line(Line2D([x + 13, x + 11], [y + 2, y + 4], color='#696969'))
    axes[4].scatter(x + 13, y + 2, size, color='pink')
    axes[4].text(x + 13, y + 2, '1', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)
    # +
    axes[4].scatter(x + 7, y + 6, size, color='#87cefa')
    axes[4].text(x + 7, y + 6, '/', verticalalignment='center', horizontalalignment='center', fontsize=fontsize)

    [line.set_zorder(0) for line in axes[4].lines]
    axes[4].legend(prop={'size': 8.5}, loc=2)


if __name__ == '__main__':
    a = '2+2'
    b = '(2+3)*4'
    c = '(7+8)*(2-1)'
    d = '(7+8)*(2-1)+7'
    e = '(7+8)*(5-2)/(2-1)'
    expressions = [a, b, c, d, e]
    result = []
    for expr in expressions:
        tree = BinaryTree.arithmetic_expr(expr)
        res = str(tree.calc())
        res = expr + ' = ' + res
        result.append(res)
        print(res)
        print(tree)
        print()

    fig, axes = plt.subplots(5, figsize=(18, 18), dpi=100)
    for j in range(5):
        axes[j].grid()
        axes[j].set_xlim((-1, 16))
        axes[j].set_ylim((-1, 8))
        axes[j].set_aspect("equal")
    graph_1()
    graph_2()
    graph_3()
    graph_4()
    graph_5()
    plt.savefig('zad_2.png', format='png')
    plt.show()

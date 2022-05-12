import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation
import sys
sys.path.insert(0, '../')
from binary_tree import BinaryTree


def draw_tree(n, mode, label, node='line', color='#000'):
    params = {
        'x': 0,
        'y': 0,
        'size': 500,
        'font-size': 15,
        'align': 'center',
        'colors': {
            'line': '#000',
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
    tmp = params['colors'][node]
    params['colors'][node] = color
    # G
    axes[n][mode].add_line(Line2D([params['x'] + 2.5, params['x'] + 2], [params['y'] + 1, params['y'] + 0],
                                  color=params['colors']['line']))
    axes[n][mode].scatter(params['x'] + 2, params['y'], params['size'], color=params['colors']['G'])
    axes[n][mode].text(params['x'] + 2, params['y'], 'G', verticalalignment=params['align'],
                       horizontalalignment=params['align'], fontsize=params['font-size'])
    # H
    axes[n][mode].add_line(Line2D([params['x'] + 6.5, params['x'] + 6], [params['y'] + 1, params['y'] + 0],
                                  color=params['colors']['line']))
    axes[n][mode].scatter(params['x'] + 6, params['y'], params['size'], color=params['colors']['H'])
    axes[n][mode].text(params['x'] + 6, params['y'], 'H', verticalalignment=params['align'],
                       horizontalalignment=params['align'], fontsize=params['font-size'])
    # I
    axes[n][mode].add_line(Line2D([params['x'] + 6.5, params['x'] + 7], [params['y'] + 1, params['y'] + 0],
                                  color=params['colors']['line']))
    axes[n][mode].scatter(params['x'] + 7, params['y'], params['size'], color=params['colors']['I'])
    axes[n][mode].text(params['x'] + 7, params['y'], 'I', verticalalignment=params['align'],
                       horizontalalignment=params['align'], fontsize=params['font-size'])
    # D
    axes[n][mode].add_line(Line2D([params['x'] + 1.5, params['x'] + 0.5], [params['y'] + 2, params['y'] + 1],
                                  color=params['colors']['line']))
    axes[n][mode].scatter(params['x'] + 0.5, params['y'] + 1, params['size'], color=params['colors']['D'])
    axes[n][mode].text(params['x'] + 0.5, params['y'] + 1, 'D', verticalalignment=params['align'],
                       horizontalalignment=params['align'], fontsize=params['font-size'])
    # E
    axes[n][mode].add_line(Line2D([params['x'] + 1.5, params['x'] + 2.5], [params['y'] + 2, params['y'] + 1],
                                  color=params['colors']['line']))
    axes[n][mode].scatter(params['x'] + 2.5, params['y'] + 1, params['size'], color=params['colors']['E'])
    axes[n][mode].text(params['x'] + 2.5, params['y'] + 1, 'E', verticalalignment=params['align'],
                       horizontalalignment=params['align'], fontsize=params['font-size'])
    # F
    axes[n][mode].add_line(Line2D([params['x'] + 5.5, params['x'] + 6.5], [params['y'] + 2, params['y'] + 1],
                                  color=params['colors']['line']))
    axes[n][mode].scatter(params['x'] + 6.5, params['y'] + 1, params['size'], color=params['colors']['F'])
    axes[n][mode].text(params['x'] + 6.5, params['y'] + 1, 'F', verticalalignment=params['align'],
                       horizontalalignment=params['align'], fontsize=params['font-size'])
    # B
    axes[n][mode].add_line(Line2D([params['x'] + 3.5, params['x'] + 1.5], [params['y'] + 3, params['y'] + 2],
                                  color=params['colors']['line']))
    axes[n][mode].scatter(params['x'] + 1.5, params['y'] + 2, params['size'], color=params['colors']['B'])
    axes[n][mode].text(params['x'] + 1.5, params['y'] + 2, 'B', verticalalignment=params['align'],
                       horizontalalignment=params['align'], fontsize=params['font-size'])
    # C
    axes[n][mode].add_line(Line2D([params['x'] + 3.5, params['x'] + 5.5], [params['y'] + 3, params['y'] + 2],
                                  color=params['colors']['line'], label=label))
    axes[n][mode].scatter(params['x'] + 5.5, params['y'] + 2, params['size'], color=params['colors']['C'])
    axes[n][mode].text(params['x'] + 5.5, params['y'] + 2, 'C', verticalalignment=params['align'],
                       horizontalalignment=params['align'], fontsize=params['font-size'])
    # A
    axes[n][mode].scatter(params['x'] + 3.5, params['y'] + 3, params['size'], color=params['colors']['A'])
    axes[n][mode].text(params['x'] + 3.5, params['y'] + 3, 'A', verticalalignment=params['align'],
                       horizontalalignment=params['align'], fontsize=params['font-size'])

    [line.set_zorder(0) for line in axes[n][mode].lines]
    axes[n][mode].legend(prop={'size': 8.5}, loc=2)
    params['colors'][node] = tmp


def animate(i):
    for j in range(4):
        axes[j][0].clear()
        axes[j][0].grid()
        axes[j][0].set_xlim((-1, 8))
        axes[j][0].set_ylim((-1, 4))
        axes[j][0].set_aspect("equal")
        axes[j][1].clear()
        axes[j][1].grid()
        axes[j][1].set_xlim((-1, 8))
        axes[j][1].set_ylim((-1, 4))
        axes[j][1].set_aspect("equal")
    # программный обход
    draw_tree(0, 0, 'Прямой обход (программный)', pre[i], '#fc3')
    draw_tree(1, 0, 'Обратный обход (программный)', post[i], '#fc3')
    draw_tree(2, 0, 'Симметричный обход (программный)', in_[i], '#fc3')
    draw_tree(3, 0, 'Обход в ширину (программный)', level[i], '#fc3')
    # ручной обход
    if i == 0:  # шаг 1
        draw_tree(0, 1, 'Прямой обход (ручной)', 'A', '#9c9')
        draw_tree(1, 1, 'Обратный обход (ручной)', 'D', '#9c9')
        draw_tree(2, 1, 'Симметричный обход (ручной)', 'D', '#9c9')
        draw_tree(3, 1, 'Обход в ширину (ручной)', 'A', '#9c9')
    elif i == 1:  # шаг 2
        draw_tree(0, 1, 'Прямой обход (ручной)', 'B', '#9c9')
        draw_tree(1, 1, 'Обратный обход (ручной)', 'G', '#9c9')
        draw_tree(2, 1, 'Симметричный обход (ручной)', 'B', '#9c9')
        draw_tree(3, 1, 'Обход в ширину (ручной)', 'B', '#9c9')
    elif i == 2:  # шаг 3
        draw_tree(0, 1, 'Прямой обход (ручной)', 'D', '#9c9')
        draw_tree(1, 1, 'Обратный обход (ручной)', 'E', '#9c9')
        draw_tree(2, 1, 'Симметричный обход (ручной)', 'G', '#9c9')
        draw_tree(3, 1, 'Обход в ширину (ручной)', 'C', '#9c9')
    elif i == 3:  # шаг 4
        draw_tree(0, 1, 'Прямой обход (ручной)', 'E', '#9c9')
        draw_tree(1, 1, 'Обратный обход (ручной)', 'B', '#9c9')
        draw_tree(2, 1, 'Симметричный обход (ручной)', 'E', '#9c9')
        draw_tree(3, 1, 'Обход в ширину (ручной)', 'D', '#9c9')
    elif i == 4:  # шаг 5
        draw_tree(0, 1, 'Прямой обход (ручной)', 'G', '#9c9')
        draw_tree(1, 1, 'Обратный обход (ручной)', 'H', '#9c9')
        draw_tree(2, 1, 'Симметричный обход (ручной)', 'A', '#9c9')
        draw_tree(3, 1, 'Обход в ширину (ручной)', 'E', '#9c9')
    elif i == 5:  # шаг 6
        draw_tree(0, 1, 'Прямой обход (ручной)', 'C', '#9c9')
        draw_tree(1, 1, 'Обратный обход (ручной)', 'I', '#9c9')
        draw_tree(2, 1, 'Симметричный обход (ручной)', 'C', '#9c9')
        draw_tree(3, 1, 'Обход в ширину (ручной)', 'F', '#9c9')
    elif i == 6:  # шаг 7
        draw_tree(0, 1, 'Прямой обход (ручной)', 'F', '#9c9')
        draw_tree(1, 1, 'Обратный обход (ручной)', 'F', '#9c9')
        draw_tree(2, 1, 'Симметричный обход (ручной)', 'H', '#9c9')
        draw_tree(3, 1, 'Обход в ширину (ручной)', 'G', '#9c9')
    elif i == 7:  # шаг 8
        draw_tree(0, 1, 'Прямой обход (ручной)', 'H', '#9c9')
        draw_tree(1, 1, 'Обратный обход (ручной)', 'C', '#9c9')
        draw_tree(2, 1, 'Симметричный обход (ручной)', 'F', '#9c9')
        draw_tree(3, 1, 'Обход в ширину (ручной)', 'H', '#9c9')
    elif i == 8:  # шаг 9
        draw_tree(0, 1, 'Прямой обход (ручной)', 'I', '#9c9')
        draw_tree(1, 1, 'Обратный обход (ручной)', 'A', '#9c9')
        draw_tree(2, 1, 'Симметричный обход (ручной)', 'I', '#9c9')
        draw_tree(3, 1, 'Обход в ширину (ручной)', 'I', '#9c9')


if __name__ == '__main__':
    f = BinaryTree('A',
                   BinaryTree('B',
                              BinaryTree('D'),
                              BinaryTree('E',
                                         BinaryTree('G')
                                         )
                              ),
                   BinaryTree('C',
                              right=BinaryTree('F',
                                               BinaryTree('H'),
                                               BinaryTree('I')
                                               )
                              )
                   )
    # программная реализация
    pre = f.pre_ordered()
    post = f.post_ordered()
    in_ = f.in_ordered()
    level = f.level_ordered()
    print('{:<20}'.format('Дерево:'), f)
    print('{:<20}'.format('Прямой обход:'), pre)
    print('{:<20}'.format('Обратный обход:'), post)
    print('{:<20}'.format('Симметричный обход:'), in_)
    print('{:<20}'.format('Обход в ширину:'), level)
    fig, axes = plt.subplots(4, 2, figsize=(14, 14), dpi=100)
    anim = FuncAnimation(fig, animate, interval=450, frames=9)
    anim.save('zad_3.gif', writer='imagemagick')
    plt.show()

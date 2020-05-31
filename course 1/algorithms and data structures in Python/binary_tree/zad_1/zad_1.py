from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from collections import deque
import sys
sys.path.insert(0, '../')
from binary_tree import BinaryTree
#             8
#       /            \
#      4             12
#    /    \        /    \
#   2      6      10    14
#  / \    / \    / \    / \
# 1   3  5   7  9  11  13 15


def tape_view(tree):
    # data
    weights = []
    tmp = deque(tree.level_ordered())
    for i in range(4):
        for j in range(2 ** i):
            tmp.popleft()
            weights.append(10 - i * 1.5)
    y = list(range(len(tree), 0, -1))
    graph = dict(zip(tree, weights))
    tree = tree.pre_ordered()
    weights = []
    for i in tree:
        weights.append(graph[i])
    ax[1].barh(y, weights, color='#009B95')
    for i in range(len(y)):
        ax[1].text(weights[i] + 0.15, y[i], tree[i], horizontalalignment='left',
                   verticalalignment='center', fontsize=22, weight='bold')


def plenty_view(tree):
    names = [str(i) for i in tree.pre_ordered()]
    width = 120
    height = 90
    ax[0].add_patch(Ellipse((0, 0), width, height,
                            color='black', alpha=0.1))
    ax[0].text(0, -35, names[0], verticalalignment='center',
               horizontalalignment='center', fontsize=48, weight='bold')

    ax[0].add_patch(Ellipse((-27, 0), width / 2.4, height / 1.4,
                            color='black', alpha=0.1))
    ax[0].text(-45, 0, names[1], verticalalignment='center',
               horizontalalignment='center', fontsize=28, weight='bold')
    ax[0].add_patch(Ellipse((27, 0), width / 2.4, height / 1.4,
                            color='black', alpha=0.1))
    ax[0].text(45, 0, names[8], verticalalignment='center',
               horizontalalignment='center', fontsize=28, weight='bold')

    ax[0].add_patch(Ellipse((-27, 15), width / 3.5, height / 3.5,
                            color='black', alpha=0.1))
    ax[0].text(-27, 6, names[2], verticalalignment='center',
               horizontalalignment='center', fontsize=18, weight='bold')
    ax[0].add_patch(Ellipse((-27, -15), width / 3.5, height / 3.5,
                            color='black', alpha=0.1))
    ax[0].text(-27, -24, names[5], verticalalignment='center',
               horizontalalignment='center', fontsize=18, weight='bold')
    ax[0].add_patch(Ellipse((27, 15), width / 3.5, height / 3.5,
                            color='black', alpha=0.1))
    ax[0].text(27, 6, names[12], verticalalignment='center',
               horizontalalignment='center', fontsize=18, weight='bold')
    ax[0].add_patch(Ellipse((27, -15), width / 3.5, height / 3.5,
                            color='black', alpha=0.1))
    ax[0].text(27, -24, names[9], verticalalignment='center',
               horizontalalignment='center', fontsize=18, weight='bold')

    ax[0].add_patch(Ellipse((19, -15), width / 9.5, height / 6,
                            color='black', alpha=0.1))
    ax[0].text(-35, 15, names[3], verticalalignment='center',
               horizontalalignment='center', fontsize=12, weight='bold')
    ax[0].add_patch(Ellipse((35, -15), width / 9.5, height / 6,
                            color='black', alpha=0.1))
    ax[0].text(-19, 15, names[4], verticalalignment='center',
               horizontalalignment='center', fontsize=12, weight='bold')
    ax[0].add_patch(Ellipse((19, 15), width / 9.5, height / 6,
                            color='black', alpha=0.1))
    ax[0].text(-35, -15, names[6], verticalalignment='center',
               horizontalalignment='center', fontsize=12, weight='bold')
    ax[0].add_patch(Ellipse((35, 15), width / 9.5, height / 6,
                            color='black', alpha=0.1))
    ax[0].text(-19, -15, names[7], verticalalignment='center',
               horizontalalignment='center', fontsize=12, weight='bold')
    ax[0].add_patch(Ellipse((-19, -15), width / 9.5, height / 6,
                            color='black', alpha=0.1))
    ax[0].text(35, -15, names[11], verticalalignment='center',
               horizontalalignment='center', fontsize=12, weight='bold')
    ax[0].add_patch(Ellipse((-35, -15), width / 9.5, height / 6,
                            color='black', alpha=0.1))
    ax[0].text(19, -15, names[10], verticalalignment='center',
               horizontalalignment='center', fontsize=12, weight='bold')
    ax[0].add_patch(Ellipse((-19, 15), width / 9.5, height / 6,
                            color='black', alpha=0.1))
    ax[0].text(35, 15, names[14], verticalalignment='center',
               horizontalalignment='center', fontsize=12, weight='bold')
    ax[0].add_patch(Ellipse((-35, 15), width / 9.5, height / 6,
                            color='black', alpha=0.1))
    ax[0].text(19, 15, names[13], verticalalignment='center',
               horizontalalignment='center', fontsize=12, weight='bold')

    ax[0].set_aspect('equal', adjustable='datalim')
    ax[0].plot()


if __name__ == '__main__':
    tree = BinaryTree(8,
                      BinaryTree(4,
                                 BinaryTree(2,
                                            BinaryTree(1), BinaryTree(3)),
                                 BinaryTree(6,
                                            BinaryTree(5), BinaryTree(7))),
                      BinaryTree(12,
                                 BinaryTree(10,
                                            BinaryTree(9), BinaryTree(11)),
                                 BinaryTree(14,
                                            BinaryTree(13), BinaryTree(15)))
                      )
    print(tree)
    fig, ax = plt.subplots(2, 1, figsize=(14, 14), dpi=80)
    ax[0].axis('off')
    ax[1].axis('off')
    plenty_view(tree)  # представление через множества
    tape_view(tree)  # ленточное представление
    plt.savefig('zad_1.png', format='png')
    plt.show()

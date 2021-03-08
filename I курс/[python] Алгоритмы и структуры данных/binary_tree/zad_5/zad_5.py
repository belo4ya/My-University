import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation
import sys
sys.path.insert(0, '../')
from binary_tree import BinaryTree


if __name__ == '__main__':
    # tree = BinaryTree(21,
    #                   BinaryTree(7,
    #                              BinaryTree(5,
    #                                         BinaryTree(4,
    #                                                    BinaryTree(2)
    #                                                    ),
    #                                         BinaryTree(6)
    #                                         ),
    #                              BinaryTree(14,
    #                                         BinaryTree(12,
    #                                                    BinaryTree(9)
    #                                                    ),
    #                                         BinaryTree(18)
    #                                         )
    #                              ),
    #                   BinaryTree(32,
    #                              BinaryTree(27,
    #                                         BinaryTree(25,
    #                                                    BinaryTree(24)
    #                                                    ),
    #                                         BinaryTree(30)
    #                                         ),
    #                              BinaryTree(37,
    #                                         BinaryTree(34,
    #                                                    BinaryTree(33)
    #                                                    ),
    #                                         BinaryTree(39)
    #                                         )
    #                              )
    #                   )
    #
    # frankenstein = BinaryTree(21)
    #
    # frankenstein.left = BinaryTree(7, parent=frankenstein)
    # frankenstein.right = BinaryTree(32, parent=frankenstein)
    #
    # frankenstein.left.left = BinaryTree(5, parent=frankenstein.left)
    # frankenstein.left.right = BinaryTree(14, parent=frankenstein.left)
    # frankenstein.right.left = BinaryTree(27, parent=frankenstein.right)
    # frankenstein.right.right = BinaryTree(37, parent=frankenstein.right)
    #
    # frankenstein.left.left.left = BinaryTree(4, parent=frankenstein.left.left)
    # frankenstein.left.left.right = BinaryTree(6, parent=frankenstein.left.left)
    # frankenstein.left.right.left = BinaryTree(12, parent=frankenstein.left.right)
    # frankenstein.left.right.right = BinaryTree(18, parent=frankenstein.left.right)
    # frankenstein.right.left.left = BinaryTree(25, parent=frankenstein.right.left)
    # frankenstein.right.left.right = BinaryTree(30, parent=frankenstein.right.left)
    # frankenstein.right.right.left = BinaryTree(34, parent=frankenstein.right.right)
    # frankenstein.right.right.right = BinaryTree(39, parent=frankenstein.right.right)
    #
    # frankenstein.left.left.left.left = BinaryTree(2, parent=frankenstein.left.left.left)
    # frankenstein.left.right.left.left = BinaryTree(9, parent=frankenstein.left.right.left)
    # frankenstein.right.left.left.left = BinaryTree(24, parent=frankenstein.right.left.left)
    # frankenstein.right.right.left.left = BinaryTree(33, parent=frankenstein.right.right.left)

    TREE_DATA = [21, 7, 32, 5, 14, 27, 37, 4, 6, 12, 18, 25, 30, 34, 39, 2, 9, 24, 33]
    INSERT_DATA = [38, 20, 8, 13, 47]
    REMOVE_DATA = [33, 14, 5, 32]

    tree = BinaryTree().create_by_arr(TREE_DATA)
    print(f'Дерево создано! Кол-во элементов: {len(tree)}')
    print(tree)
    print()
    for i in INSERT_DATA:
        tree.insert(i)
        print(f'\nЭлемент {i} успешно вставлен! (Кол-во элементов: {len(tree)})')
        print(tree)
    print(f'\nТекущее дерево. Кол-во элементов: {len(tree)}')
    print(tree)
    input('\ncontinue? ')
    for i in REMOVE_DATA:
        tree.del_node_by_value(i)
        print(f'\nЭлемент {i} успешно удален! (Кол-во элементов: {len(tree)})')
        print(tree)
    print(f'\nТекущее дерево. Кол-во элементов: {len(tree)}')
    print(tree)

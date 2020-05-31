from collections import deque


class TreeError(Exception):

    def __init__(self, text='Error'):
        self.text = text


class BinaryTree:

    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return '{} ({}, {})'.format(str(self.value), str(self.left), str(self.right))

    def __repr__(self):
        return '{} ({}, {})'.format(str(self.value), str(self.left), str(self.right))

    def __iter__(self):
        return iter(self.level_ordered())

    def __len__(self):
        return len(self.level_ordered())

    # def tree_print(self, node, dir, level):  # Хорошая реализация, но нет
    #     if node:
    #         print(f'lvl {level} {dir} = {node.value}')
    #         self.tree_print(node.left, 'left', level+1)
    #         self.tree_print(node.right, 'right', level+1)

    def insert_left(self, child=None):
        if self.left:
            child = BinaryTree(child)
            child.left = self.left
            self.left = child
        else:
            self.left = BinaryTree(child)

    def insert_right(self, child=None):
        if self.right:
            child = BinaryTree(child)
            child.right = self.right
            self.right = child
        else:
            self.right = BinaryTree(child)

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_root_val(self, new_root):
        self.value = new_root

    def get_root_val(self):
        return self.value

    def list_view(self):
        """Представление дерева в виде списка списков"""
        return [i for i in self._list_view() if not isinstance(i, BinaryTree)]

    def _list_view(self):
        s = [self.value, self.right, self.left]
        if self.left:
            s.append(self.left.list_view())
        if self.right:
            s.append(self.right.list_view())
        return s

    def level_ordered(self):
        """Горизонтальный обход (в ширину)"""
        queue = deque()
        iter_ = []
        node = self
        queue.append(node)
        while len(queue):
            node = queue.popleft()
            iter_.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return iter_

    def pre_ordered(self):
        """
        Вертикальный обход (в глубину) прямой
        Node -> Left -> Right
        """
        stack = []
        iter_ = []
        node = self
        stack.append(node)
        while len(stack):
            node = stack.pop()
            iter_.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return iter_

    def post_ordered(self):
        """
        Вертикальный обход (в глубину) обратный (концевой)
        Left -> Right -> Node
        """
        stack = []
        iter_ = []
        node = self
        lnp = None
        while len(stack) or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack[-1]
                if peek.right and lnp != peek.right:
                    node = peek.right
                else:
                    stack.pop()
                    iter_.append(peek.value)
                    lnp = peek
        return iter_

    def in_ordered(self):
        """
        Вертикальный обход (в глубину) симметричный (поперечный, обратный)
        Left -> Node -> Right
        """
        stack = []
        iter_ = []
        node = self
        while len(stack) or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                iter_.append(node.value)
                node = node.right
        return iter_

    @staticmethod
    def arithmetic_expr(expr):
        """
        Создает объект класса BinaryTree, который является
        деревом представления арифметического выражения
        """
        try:
            node = BinaryTree()
            stack = [node]
            expr = [i for i in expr if i != ' ']
            for i in expr:
                if i == '(':
                    if node.left:
                        stack.append(node)
                        node.insert_right()
                        node = node.right
                    else:
                        stack.append(node)
                        node.insert_left()
                        node = node.left
                elif i in ['+', '-', '/', '*']:
                    if node.value:
                        node = BinaryTree(i, node)
                        stack = []
                    else:
                        node.value = i
                elif i.isdigit():
                    if node.left:
                        stack.append(node)
                        node.insert_right()
                        node = node.right
                        node.value = i
                        node = stack.pop()
                    else:
                        stack.append(node)
                        node.insert_left()
                        node = node.left
                        node.value = i
                        node = stack.pop()
                elif i == ')':
                    node = stack.pop()
            if node.value is None:
                node = node.left
            return node

        except (ValueError, TypeError, IndexError):
            raise TreeError('Неверное арифметическое выражение!')

    def calc(self):
        """
        Выполняет вычисления, если объект являтся
        представлением арифметического выражения
        """
        try:
            res = 0
            op_stack = []
            digit_stack = deque()
            for i in self.level_ordered():
                if i in ['+', '-', '/', '*']:
                    op_stack.append(i)
                elif i.isdigit():
                    digit_stack.append(i)
            while len(digit_stack) > 1:
                op = op_stack.pop()
                operand2 = int(digit_stack.pop())
                operand1 = int(digit_stack.pop())
                if op == '+':
                    res = operand1 + operand2
                elif op == '-':
                    res = operand1 - operand2
                elif op == '/':
                    res = operand1 / operand2
                else:
                    res = operand1 * operand2
                digit_stack.appendleft(res)
            return res

        except (ValueError, TypeError, IndexError):
            raise TreeError('Дерево должно быть представление арифметического выражения!')

    # Методы для работы с бинарным деревом поиска

    @staticmethod
    def create_by_arr(arr):
        """
        Создание Бинарного дерева поиска по входным данным
        Время: O(n*log n) + сортировка
        """
        tree = BinaryTree(arr[0])
        for i in arr[1:]:
            tree.insert(i)
        return tree

    @staticmethod
    def create_by_sort_arr(arr):
        """
        Создание сбалансированного Бинарного дерева поиска
        Время: O(log n) + сортировка
        """
        srt_arr = sorted(arr)
        return BinaryTree()._create_by_sort_arr(srt_arr, 0, len(srt_arr) - 1)

    def _create_by_sort_arr(self, arr, start, end):
        """
        Рекурсия:
            Создается левое поддерево из левой части массива
            Создается правое поддерево из правой части массива
        """
        if end < start:
            return None
        mid = (start + end) // 2
        node = BinaryTree(arr[mid])
        node.left = self._create_by_sort_arr(arr, start, mid - 1)
        node.right = self._create_by_sort_arr(arr, mid + 1, end)
        return node

    def find(self, node, target):
        """Рекурсивный поиск элемента в Бинарном дереве поиска"""
        if node is None:
            return None
        else:
            if target == node.value:
                return node
            else:
                if target < node.value:
                    return self.find(node.left, target)
                else:
                    return self.find(node.right, target)

    def iter_find(self, target):
        """Итеративный поиск элемента в Бинарном дереве поиска"""
        stack = []
        node = self
        while node:
            stack.append(node.value)
            if target < node.value:
                node = node.left
                continue
            elif target > node.value:
                node = node.right
                continue
            else:
                return node, stack

    def insert(self, value):
        """Вставка элемента в Бинарном дерево поиска"""
        node = self
        if self.find(node, value):
            return 0
        if self.left or self.right or self.value:
            self._insert(node, value)
        else:
            self.value = value
        return 1

    def _insert(self, node, value):
        """Рекурсивная вставка"""
        if value < node.value:
            if node.left is None:
                node.left = BinaryTree(value, parent=node)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = BinaryTree(value, parent=node)
            else:
                self._insert(node.right, value)

    def del_node_by_value(self, value):
        """Удаление узла по его значению"""
        node = self.find(self, value)
        self._del_node(node)
        return 1

    def _del_node(self, node):
        """Удаление выбранного узла"""
        if node is None:
            return None
        elif node.left and node.right:  # случай: два наследника
            cur_node = node.right
            while cur_node.left:
                cur_node = cur_node.left
            if cur_node.right:  # если наименьший узел не лист
                if node.parent.left == node:
                    node.parent.left.value = cur_node.value
                else:
                    node.parent.right.value = cur_node.value
                if cur_node.parent.left == cur_node:
                    cur_node.parent.left = cur_node.parent.left.right
                else:
                    cur_node.parent.right = cur_node.parent.right.right
                    return  # очень сомнительно, но работает
            else:  # если наименьший узел лист
                if node.parent.left == node:
                    node.parent.left.value = cur_node.value
                else:
                    node.parent.right.value = cur_node.value
            # удалить cur_node
            if cur_node.parent.left == cur_node:
                cur_node.parent.left = None
            else:
                cur_node.parent.right = None
        elif node.left:  # случай: есть только левый узел
            if node == node.parent.left:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        elif node.right:  # случай: есть только правый узел
            if node == node.parent.right:
                node.parent.right = node.right
            else:
                node.parent.left = node.right
        else:  # случай: лист
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

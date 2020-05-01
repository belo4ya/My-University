from collections import deque


class MDLinkedList:
    """
    Двусвязный список на основе deque (двусторонней очереди)
    """

    def __init__(self, iterable):
        self.link_list = deque(iterable)

    def append(self, item):
        return self.link_list.append(item)

    def appendleft(self, item):
        return self.link_list.appendleft(item)

    def pop(self):
        return self.link_list.pop()

    def popleft(self):
        return self.link_list.popleft()

    def insert(self, index, item):
        return self.link_list.insert(index, item)

    def remove(self, value):
        return self.link_list.remove(value)

    def copy(self):
        return self.link_list.copy()

class Empty(Exception):
    pass


class DoublyLinkedList:
    class _Node:

        def __init__(self, previous, next, data):
            self._prev = previous
            self._next = next
            self._data = data

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, element):
        node = self._Node(None, None, element)
        if self.is_empty():
            self._head = self._tail = node
        else:
            self._head._prev = node
            node._next = self._head
            self._head = node
        self._size += 1

    def add_last(self, element):
        node = self._Node(None, None, element)
        if self.is_empty():
            self._head = self._tail = node
        else:
            self._tail._next = node
            node._prev = self._tail
            self._tail = node
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty('')

        rtn_element = self._head._data
        temp_node = self._head
        self._head = self._head._next
        temp_node = None
        self._size -= 1
        return rtn_element

    def remove_last(self):
        if self.is_empty():
            raise Empty('')

        rtn_element = self.tail._data
        temp_node = self._tail
        self._tail = self._tail._prev
        self._tail._next = None
        temp_node = None
        self._size -= 1
        return rtn_element

    def insert(self, index, value):
        if self.is_empty():
            self.add_first(value)
        elif index == 0:
            self.add_first(value)
        elif index == self._size:
            self.add_last(value)
        else:
            marker = self._head
            node = self._Node(None, None, value)
            for i in range(self._size):
                if i == index:
                    node._prev = marker
                    node._next = marker._next
                    marker._next = node
                    break
                marker = marker._next
        self._size += 1

    def remove(self, value):
        if self.is_empty():
            raise Empty('')

        marker = self._head
        for i in range(self._size):
            if marker._data == value:
                prev = marker._prev
                next = marker._next
                prev._next = next
                next._prev = prev
                marker = None
                self._size -= 1
                return
            else:
                marker = marker._next

    def print(self):
        current = self._head
        i = 0
        while current != None:
            print(f"item {i} value {current._data}")
            i += 1
            current = current._next
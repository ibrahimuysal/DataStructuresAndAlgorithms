class Empty(Exception):
    pass


class SinglyLinkedList:
    class _Node:
        def __init__(self, data, next):
            self._data = data
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, element):
        if self.is_empty():
            self._head = self._tail = self._Node(element, None)
        else:
            self._head = self._Node(element, self._head)
        self._size += 1

    def add_last(self, element):
        node = self._Node(element, None)
        if self.is_empty():
            self._head = self._tail = node
        else:
            self._tail._next = node
            self._tail = node
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty('')

        rtn_element = self._head._data
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head._next

        self._size -= 1
        return rtn_element

    def remove_last(self):
        if self.is_empty():
            raise Empty('')

        rtn_element = self._tail._data
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            temp = self._head
            while temp.next != self._tail:
                temp = temp.next
            self._tail = temp
            self._tail._next = None

        self._size -= 1
        return rtn_element

    def print(self):
        current = self._head
        for i in range(self._size):
            print(f"item {i} value {current._data}")
            current = current._next

    def get_first_element(self):
        if not self.is_empty():
            return self._head._data
        return None


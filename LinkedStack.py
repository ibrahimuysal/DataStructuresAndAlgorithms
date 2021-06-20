from SinglyLinkedList import *


class LinkedStack:

    def __init__(self):
        self._linkedList = SinglyLinkedList()
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, value):
        self._linkedList.add_first(value)
        self._size += 1

    def pop(self):
        self._size -= 1
        return self._linkedList.remove_first()

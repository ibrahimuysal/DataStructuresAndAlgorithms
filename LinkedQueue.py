from SinglyLinkedList import *


class LinkedQueue:

    def __init__(self):
        self._linkedList = SinglyLinkedList()
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, value):
        self._linkedList.add_last(value)
        self._size += 1

    def dequeue(self):
        self._size -= 1
        return self._linkedList.remove_first()

    def peek(self):
        return self._linkedList.get_first_element()

    def poll(self):
        if not self.is_empty():
            return self._linkedList.remove_first()
        return None


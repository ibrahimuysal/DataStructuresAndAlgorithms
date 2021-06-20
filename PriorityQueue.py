class PriorityQueue:
    """
    PriorityQueue ADT implementation with BinaryHeap(Complete Binary Tree), Python List is used as storage
    Heap Invariant:
        Min-Heaps: parent key is less than equal to  its children
        Max-Heaps: parent key is greater than equal to  its children
    """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def add(self, element):
        self._data.append(element)  # element added last index in List(array) based implementation
        self._bubble_up(len(self._data) - 1)  # bubbleUp from last added item (last index) to satisfy heap invariant

    def min(self):
        # Min-Heaps invariant root is the minimum value. List(array implementation at index 0)
        if not self.is_empty():
            return self._data[0]
        return None

    def poll(self):
        if not self.is_empty():
            self._swap(0, len(self._data) - 1)  # swap root (index 0) and last node (last index in array)
            rtn_element = self._data.pop()
            self._bubble_down(0)  # bubbleDown from root (index 0) to satisfy heap invariant
            return rtn_element
        return None

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def _has_left(self, index):
        return self._left(index) < len(self._data)

    def _has_right(self, index):
        return self._right(index) < len(self._data)

    def _swap(self, index1, index2):
        self._data[index1], self._data[index2] = self._data[index2], self._data[index1]

    def _bubble_up(self, index):
        parent = self._parent(index)
        if index > 0 and self._data[index] < self._data[parent]:
            self._swap(index, parent)
            self._bubble_up(parent)

    def _bubble_down(self, index):
        if self._has_left(index):
            left = self._left(index)
            smaller = left
            if self._has_right(index):
                right = self._right(index)
                if self._data[left] > self._data[right]:
                    smaller = right
            if self._data[smaller] < self._data[index]:
                self._swap(index, smaller)
                self._bubble_down(smaller)

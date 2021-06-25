class Node:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None
        self._height = 1

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def has_left(self):
        return self._left is not None

    def has_right(self):
        return self._right is not None

    def is_leaf(self):
        return (self._left is None) and (self._right is None)
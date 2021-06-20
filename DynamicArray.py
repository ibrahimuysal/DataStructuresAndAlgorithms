import ctypes


class _DynamicArray:

    def __init__(self):
        self._capacity = 1
        self._n = 0
        self._data = self._make_array(self._capacity)
        self.itr_count = 0

    def __len__(self):
        return self._n

    def __next__(self):
        try:
            item = self._data[self.itr_count]
        except IndexError:
            raise StopIteration
        self.itr_count += 1
        return item

    def __iter__(self):
        return self

    def __get_item(self, index):
        if not 0 <= index < self._n:
            raise IndexError
        return self._data[index]

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def _resize(self, capacity):
        temp = self._make_array(capacity)
        self._capacity = capacity
        for i in range(self._n):
            temp[i] = self._data[i]
        self._data = temp

    def append(self, element):
        if self._capacity == self._n:
            self._resize(2 * self._capacity)
        self._data[self._n] = element
        self._n += 1

    def insert(self, index, value):
        if self._capacity == self._n:
            self._resize(2 * self._capacity)
        for i in range(self._n, index, -1):  # shift rightmost
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._n += 1

    def remove(self, value):
        for i in range(self._n):
            if self._data[i] == value:
                for k in range(self._n - i - 1):
                    self._data[i + k] = self._data[i + k + 1]
                self._n -= 1
                self._data[self._n] = None
                return
        raise ValueError('value not found')

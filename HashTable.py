class HashTable:
    """
    Simple HashTable implementation - for quick refresher -
    - separate chaining
    """

    class _Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value
            self._next = None

        def __hash__(self):
            return hash(self._key)

        def __add__(self, other):
            self._next = other

        def __repr__(self):
            return f'Item key is {self._key} and Value is: {self._value}'

    HT_SIZE = 5

    def __init__(self):
        self._size = 0
        self._list = [None] * self.HT_SIZE

    def __len__(self):
        return self._size

    def __setitem__(self, key, value):
        self._size += 1
        item = self._Item(key, value)
        index = self._hash_function(item)
        if self._list[index] is None:
            self._list[index] = item
        elif self._list[index]._key is item._key:
            self._list[index]._value = item._value
        elif self._list[index]._key is not item._key:
            self._list[index] + item
        else:
            self._size -= 1

    def __getitem__(self, key):
        item = self._Item(key, None)
        index = self._hash_function(item)

        if self._list[index] is None:
            return None
        elif self._list[index]._key == key:
            return self._list[index]
        elif self._list[index]._key != key:
            marker = self._list[index]
            while marker._key is not None:
                if marker._key == key:
                    return marker
                marker = marker._next
        else:
            return None

    def __delitem__(self, key):
        item = self._Item(key, None)
        index = self._hash_function(item)

        if self._list[index] is not None and self._list[index]._key == key:
            self._list[index] = None
            self._size -= 1

    def _hash_function(self, item):
        return hash(item) % self.HT_SIZE



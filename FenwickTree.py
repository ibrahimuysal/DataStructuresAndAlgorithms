import copy


class FenwickTree:
    """
     Fenwick Tree or Binary Indexed Tree - Prefix Sum
    """

    def __init__(self, arr):
        self._bitree = [0]  # root node of the fenwick tree
        self._bitree += copy.deepcopy(arr)
        for i in range(len(self._bitree)):
            j = i + self._lsb(i)
            if j <= len(self._bitree):
                self._bitree[j] = self._bitree[j] + self._bitree[i]

    def __len__(self):
        return len(self._bitree)

    def add(self, index, delta):
        while index < len(self._bitree):
            self._bitree[index] += delta
            index += self._lsb(index)

    def prefix_sum(self, index):
        sum = 0
        while index != 0:
            sum += self._bitree[index]
            index -= self._lsb(index)
        return sum

    def range_query(self, _from, _to):
        if _from < 0 and _from > len(self._bitree):
            raise IndexError
        if _to < 0  and _to > len(self._bitree):
            raise IndexError
        return self.prefix_sum(_to) - self.prefix_sum(_from - 1)

    def _lsb(self, index):
        return index & (-index)



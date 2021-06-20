class BinarySearchTree:
    class _Node:
        def __init__(self, data):
            self._data = data
            self._left = None
            self._right = None

        def _has_left(self):
            return self._left is not None

        def _has_right(self):
            return self._right is not None

        def _is_leaf(self):
            return (self._left is None) and (self._right is None)

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        self._print_inorder(self._root)

    def is_empty(self):
        return self._size == 0

    def add(self, value):
        node = self._Node(value)
        if self.is_empty():
            self._root = node
            self._size += 1
            return
        self._insert(self._root, node)

    def remove(self, value):
        if self.is_empty():
            print('BST is empty')
            return
        self._delete_Node(self._root, value)

    def _delete_Node(self, root, value):
        if value < root._data:
            root._left = self._delete_Node(root._left, value)
        elif value > root._data:
            root._right = self._delete_Node(root._right, value)
        elif value == root._data:
            if root._is_leaf():
                root = None
                self._size -= 1
            elif root._has_right():
                root = self._get_successor(root)
                self._size -= 1
            else:
                root = self._get_predecessor(root)
                self._size -= 1

        return root

    def _get_successor(self, root):
        """right then always left"""
        root = root._right
        while root._has_left():
            root = root._left

        return root

    def _get_predecessor(self, root):
        """left then always right"""
        root = root._left
        while root._has_right():
            root = root._right
        return root

    def _insert(self, root, node):
        if (not root._has_left()) and node._data < root._data:
            root._left = node
            self._size += 1
        elif (not root._has_right()) and node._data > root._data:
            root._right = node
            self._size += 1
        elif node._data < root._data:
            self._insert(root._left, node)
        elif node._data > root._data:
            self._insert(root._right, node)
        else:
            return

    def _print_inorder(self, node):
        if node is None:
            return
        self._print_inorder(node._left)
        print(node._data)
        self._print_inorder(node._right)

    def _print_preorder(self, node):
        if node is None:
            return
        print(node._data)
        self._print_inorder(node._left)
        self._print_inorder(node._right)

    def _print_postorder(self, node):
        if node is None:
            return
        self._print_inorder(node._left)
        self._print_inorder(node._right)
        print(node._data)

from Node import *


class BinarySearchTree:

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
        node = Node(value)
        if self.is_empty():
            self._root = node
            self._size += 1
            return node
        self._insert(self._root, node)

    def remove(self, value):
        if self.is_empty():
            print('BST is empty')
            return
        self._delete_Node(self._root, value)

    def _delete_Node(self, root, value):
        if root is None:
            return root

        if value < root.data:
            root.left = self._delete_Node(root.left, value)
        elif value > root.data:
            root.right = self._delete_Node(root.right, value)
        elif value == root.data:
            if root.is_leaf():
                root = None
                self._size -= 1
                return root
            elif root.has_right():
                successor = self._get_successor(root)
                root.data = successor.data
                root.right = self._delete_Node(root.right, root.data)
            else:
                predecessor = self._get_predecessor(root)
                root.data = predecessor.data
                root.left = self._delete_Node(root.left, root.data)

        return root

    def _get_successor(self, root):
        """right then always left"""
        root = root.right
        while root.has_left():
            root = root.left

        return root

    def _get_predecessor(self, root):
        """left then always right"""
        root = root.left
        while root.has_right():
            root = root.right
        return root

    def _insert(self, root, node):
        if (not root.has_left()) and node.data < root.data:
            root.left = node
            self._size += 1
        elif (not root.has_right()) and node.data > root.data:
            root._right = node
            self._size += 1
        elif node.data < root.data:
            root.left = self._insert(root.left, node)
        else:
            root.right = self._insert(root.right, node)

        return root

    def _print_inorder(self, node):
        if node is None:
            return
        self._print_inorder(node.left)
        print(node.data)
        self._print_inorder(node.right)

    def _print_preorder(self, node):
        if node is None:
            return
        print(node.data)
        self._print_inorder(node.left)
        self._print_inorder(node.right)

    def _print_postorder(self, node):
        if node is None:
            return
        self._print_inorder(node.left)
        self._print_inorder(node.right)
        print(node.data)

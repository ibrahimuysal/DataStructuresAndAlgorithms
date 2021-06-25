from BinarySearchTree import *


class AVLTree(BinarySearchTree):

    def _insert(self, root, node):
        super()._insert(root, node)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance_factor = self.get_balance_factor(root)
        if balance_factor > 1:
            if node.data < root.left.data:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if node.data > root.right.data:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        self._root = root
        return root

    def remove(self, value):
        if self.is_empty():
            print('AVL is empty')
            return
        self._delete_Node_AVL(self._root, value)

    def _delete_Node_AVL(self, root, value):
        super()._delete_Node(root, value)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance_factor = self.get_balance_factor(root)
        if balance_factor > 1:
            if self.get_balance_factor(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance_factor < -1:
            if self.get_balance_factor(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance_factor(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    #
    #                    T1, T2 and T3 are subtrees of the tree
    #
    #                     B                               A
    #                    / \     Right Rotation          /  \
    #                   A   T3   - - - - - - - >        T1   B
    #                  / \       < - - - - - - -            / \
    #                 T1  T2     Left Rotation            T2  T3
    #
    #                 keys(T1) < key(x) < keys(T2) < key(y) < keys(T3)
    #
    def left_rotate(self, A):
        B = A.right
        T2 = B.left

        B.left = A
        A.right = T2

        A.height = 1 + max(self.get_height(A.left), self.get_height(A.right))
        B.height = 1 + max(self.get_height(B.left), self.get_height(B.right))

        return B

    def right_rotate(self, B):
        A = B.left
        T2 = A.right

        A.right = B
        B.left = T2

        B.height = 1 + max(self.get_height(B.left), self.get_height(B.right))
        A.height = 1 + max(self.get_height(A.left), self.get_height(A.right))

        return A

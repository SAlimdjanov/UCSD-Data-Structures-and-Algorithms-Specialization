""" 
tree_orders.py

"""

import sys
import threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    """
    Tree Orders class

    """

    def __init__(self):
        self.num_n = 0
        self.key = 0
        self.left = 0
        self.right = 0

    def read(self):
        """
        Read and store inputs accordingly

        """
        self.num_n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.num_n)]
        self.left = [0 for i in range(self.num_n)]
        self.right = [0 for i in range(self.num_n)]
        for i in range(self.num_n):
            [num_a, num_b, num_c] = map(int, sys.stdin.readline().split())
            self.key[i] = num_a
            self.left[i] = num_b
            self.right[i] = num_c

    def in_order(self, root):
        """
        In-order tree traversal

        Args:
            root (int): Tree root node

        """
        if root == -1:
            return []
        self.in_order(self.left[root])  # type: ignore
        print(self.key[root], end=" ")  # type: ignore
        self.in_order(self.right[root])  # type: ignore

    def pre_order(self, root):
        """
        Pre-order tree traversal

        Args:
            root (int): Tree root node

        """
        if root == -1:
            return []
        print(self.key[root], end=" ")  # type: ignore
        self.pre_order(self.left[root])  # type: ignore
        self.pre_order(self.right[root])  # type: ignore

    def post_order(self, root):
        """
        Post-order tree traversal

        Args:
            root (int): Tree root node

        """
        if root == -1:
            return []
        self.post_order(self.left[root])  # type: ignore
        self.post_order(self.right[root])  # type: ignore
        print(self.key[root], end=" ")  # type: ignore


def main():
    """
    Main method

    """
    tree = TreeOrders()
    tree.read()
    if tree is not None:
        tree.in_order(0)
        print()
        tree.pre_order(0)
        print()
        tree.post_order(0)
        print()


threading.Thread(target=main).start()

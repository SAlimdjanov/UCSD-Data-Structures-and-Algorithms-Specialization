""" 
is_bst.py

"""

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class Node:
    """
    Creates a node with left and right children

    """

    def __init__(self, num_i, num_j, num_k):
        self.key = num_i
        self.left = num_j
        self.right = num_k


def is_binary_search_tree(tree):
    """
    Checks if the input tree is a binary search tree

    Args:
        tree (list): List of nodes

    Returns:
        bool: True/False

    """
    _stack = [(float("-inf"), tree[0], float("inf"))]
    while _stack:
        _min, root, _max = _stack.pop()
        if root.key < _min or root.key >= _max:
            return False
        if root.left != -1:
            _stack.append((_min, tree[root.left], root.key))
        if root.right != -1:
            _stack.append((root.key, tree[root.right], _max))
    return True


def main():
    """
    Main method

    """
    num_nodes = int(input())
    nodes = [0 for _ in range(num_nodes)]
    for val in range(num_nodes):
        i, j, k = map(int, input().split())
        node = Node(i, j, k)
        nodes[val] = node  # type: ignore
    if num_nodes == 0 or is_binary_search_tree(nodes):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()

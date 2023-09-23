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


def in_order_traversal(tree):
    """
    In-order traversal of input tree

    Args:
        tree (list): List of nodes

    Returns:
        list: List of values from in-order traversal
    """
    _stack, result, current = [], [], 0
    while _stack or current != -1:
        if current != -1:
            root = tree[current]
            _stack.append(root)
            current = root.left
        else:
            root = _stack.pop()
            result.append(root.key)
            current = root.right
    return result


def is_binary_search_tree(tree, num_n):
    """
    Checks if the input tree is a binary search tree

    Args:
        tree (list): List of nodes
        num_n (int): Number of nodes

    Returns:
        bool: True/False

    """
    nodes = in_order_traversal(tree)
    for i in range(1, num_n):
        if nodes[i] <= nodes[i - 1]:
            return False
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
    if num_nodes == 0 or is_binary_search_tree(nodes, num_nodes):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()

"""
tree_height.py

"""

import sys
import threading


class Tree:
    """
    Tree class to store left and right values

    """

    def __init__(self, value):
        self.value = value
        self.children = []


def create_tree(parents):
    """
    Creates the tree

    Args:
        parents (int list): Integer list of parents

    Returns:
        int: root of the tree

    """
    len_parents, root = len(parents), None
    nodes_list = [Tree(i) for i in range(len_parents)]

    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes_list[i]
        else:
            nodes_list[parent].children.append(nodes_list[i])

    return root


def compute_height(tree, mem_dict):
    """
    Compute tree height given the root of a tree

    Args:
        tree (class Tree): Root of the tree
        mem_dict (dictionay): Dictionary to memorize results

    Returns:
        int: Height of the tree
    """
    if tree is None:
        return 0

    if tree.value in mem_dict:
        return mem_dict[tree.value]

    max_child_height = 0
    for child in tree.children:
        child_height = compute_height(child, mem_dict)
        max_child_height = max(max_child_height, child_height)

    height = 1 + max_child_height
    mem_dict[tree.value] = height
    return height


def main():
    """
    main method

    """
    _ = int(input())
    parents = list(map(int, input().split()))
    memorization_dict = {}
    root = create_tree(parents)
    height = compute_height(root, memorization_dict)
    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()

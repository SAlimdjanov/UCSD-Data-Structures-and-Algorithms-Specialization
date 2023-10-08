# python3

""" 
plan_party.py

Invite people from your company to a party in such a way that everybody is relaxed, because the 
direct boss of any invited person is not invited.

"""

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Node:
    """Creates a Node object"""

    def __init__(self, weight):
        self.weight = weight
        self.children = []


def read_data():
    """Read input data and construct a tree"""
    _size = int(input())
    _tree = [Node(_w) for _w in map(int, input().split())]
    for _ in range(1, _size):
        _a, _b = list(map(int, input().split()))
        _tree[_a - 1].children.append(_b - 1)
        _tree[_b - 1].children.append(_a - 1)
    return _tree


def dfs(_tree, _current_vertex, _parent, _dynamic_table):
    """Perform DFS on a _tree and calculate the maximum achievable value"""
    if _dynamic_table[_current_vertex] == -1:
        if len(_tree[_current_vertex].children) == 1 and _current_vertex != 0:
            _dynamic_table[_current_vertex] = _tree[_current_vertex].weight
        else:
            m_f = _tree[_current_vertex].weight
            for u in _tree[_current_vertex].children:
                if u != _parent:
                    for w in _tree[u].children:
                        if w != _current_vertex:
                            m_f += dfs(_tree, w, u, _dynamic_table)
            m_i = 0
            for u in _tree[_current_vertex].children:
                if u != _parent:
                    m_i += dfs(_tree, u, _current_vertex, _dynamic_table)
            _dynamic_table[_current_vertex] = max(m_i, m_f)
    return _dynamic_table[_current_vertex]


def max_weight_indep_tree_subset(_tree):
    """Calculates the maximum weight of an independent subset of vertices in a tree"""
    _size = len(_tree)
    if _size == 0:
        return 0
    _dynamic_table = [-1] * _size
    return dfs(_tree, 0, -1, _dynamic_table)


def main():
    """Main method for threading"""
    _tree = read_data()
    _weight = max_weight_indep_tree_subset(_tree)
    print(_weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()

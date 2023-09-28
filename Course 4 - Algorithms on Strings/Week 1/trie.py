# python3

"""
trie.py

Return the trie built from patterns in the form of a dictionary of dictionaries, for example: 

{0:{'A':1,'T':2},1:{'C':3}}

Where the key of the external dictionary is the node ID (integer), and the internal dictionary 
contains all the trie edges outgoing from the corresponding node, and the keys are the letters on 
those edges, and the values are the node IDs to which these edges lead.

"""


def build_trie(_patterns):
    """
    Build a trie with a list of input patterns

    Args:
        _patterns (list): List of patterns containing capital letters A, C, G, T only.

    Returns:
        dict: Dictionary of the form:
              {node_i: {'character': node_f} ... node_(n - 1): {'character': node_f}}
              Where node_i is the starting point of the edge, 0 <= i <= (n - 1), where n is the
              number of nodes (input patterns). node_f is the end point of the edge.

    """
    _tree, _node = {}, 0
    for _pattern in _patterns:
        _current, _len_pattern = 0, len(_pattern)
        for i in range(_len_pattern):
            _char = _pattern[i]
            if _current in _tree and _char in _tree[_current]:
                _current = _tree[_current].get(_char)
            else:
                _node = _node + 1
                if _current not in _tree:
                    _tree[_current] = {}
                    _tree[_current][_char] = _node
                else:
                    _tree[_current][_char] = _node
                _current = _node
    return _tree


if __name__ == "__main__":
    nodes = int(input())
    patterns = []
    for _ in range(nodes):
        pattern = input()
        patterns.append(pattern)
    tree = build_trie(patterns)
    # Note: Iteration with items works locally, but not on Coursera's grading machine
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

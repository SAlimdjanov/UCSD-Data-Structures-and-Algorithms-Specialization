# python3

"""
trie.py

Finds all starting positions in Text where a string from Patterns appears as a substring in
increasing order (assuming that Text is a 0-based array of symbols)

"""


def prefix_match(_text, _trie):
    """Checks if a character is an element of the Trie"""
    _v, _len_text = 0, len(_text)
    for i in range(_len_text):
        _char = _text[i]
        if _char in _trie[_v]:
            _v = _trie[_v][_char]
            if _v not in _trie:
                return True
        else:
            return False


def trie_matching(_text, _trie):
    """Returns list of indices where prefix match begins"""
    _indices, _len_text = [], len(_text)
    for j in range(_len_text):
        _is_prefix = prefix_match(_text[j:], _trie)
        if _is_prefix:
            _indices.append(j)
    return _indices


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
    text = input()
    nodes = int(input())
    patterns = []
    for _ in range(nodes):
        pattern = input()
        patterns.append(pattern)
    tree = build_trie(patterns)
    indices = trie_matching(text, tree)
    for index in indices:
        print(index, end=" ")

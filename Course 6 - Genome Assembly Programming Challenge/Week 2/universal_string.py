# python3

""" 
k_univ_circ_string.py

Finds a k-universal circular binary string.

"""

from collections import defaultdict


def create_adjacencies(_k):
    """Generate adjacency dictionary given _k, the binary graph size."""
    _pos, _last = _k - 1, "1" * _k
    _bin_int = int(_last, 2)
    _last_before, _first = "1" + ("0" * _pos), "0" * _k
    _nodes = defaultdict(list)
    for i in range(0, _bin_int + 1):
        _bin_str = bin(i)[2:].zfill(_k)
        if _bin_str not in (_last_before, _first):
            string = _bin_str[0:_pos]
            edge = _bin_str[1:_k]
            _nodes[string].append(edge)
            _nodes[edge].append(string)
    return _nodes


def generate_tours(_k, _nodes):
    """Generates a tour given a value _k and adjacency dictionary _nodes"""
    _start = "0" * (_k - 1)
    _tour = [_start]
    _curr = _start
    while len(_nodes[_curr]) > 0:
        _suffix = _curr[1:]
        _next_char = "1" if _suffix + "1" in _nodes[_curr] else "0"
        _tour.append(_suffix + _next_char)
        _nodes[_curr].remove(_suffix + _next_char)
        _nodes[_suffix + _next_char].remove(_curr)
        _curr = _suffix + _next_char
    return _tour


if __name__ == "__main__":
    k = int(input())
    nodes = create_adjacencies(k)
    tour = generate_tours(k, nodes)
    RESULT = "0"
    for _, char in enumerate(tour):
        RESULT += char[0]
    print(RESULT)

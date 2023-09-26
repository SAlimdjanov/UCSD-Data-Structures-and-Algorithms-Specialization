""" 
shortest_paths.py

Uses a barebone graph implementation as there currently are issues when using the Graph ADT 
implementation.

TODO: Update solution if Graph ADT implementation is fixed.

"""

from collections import deque


def modified_bellman_ford(_num_v, _edges, _adjacencies, _start):
    """
    Perform the Bellman-Ford Algorithm to check for a negative cycle in a given graph.

    Args:
        _num_v (int): Number of vertices
        _edges (list): 2D list containing edges of the form [start, end, weight]
        _adjacencies (list): 2D list contain the start vertex and elements of the form [end, weight]
        _start (int): Start vertex

    Returns:
        list: List of resulting path distances.

    """
    _results = [float("inf")] * (_num_v + 1)
    _results[_start] = 0
    _previous = [None] * (_num_v + 1)
    _negative_nodes = deque()
    for _i in range(_num_v):
        for _u, _v, _w in _edges:
            if _results[_v] > _results[_u] + _w:
                _results[_v] = _results[_u] + _w
                _previous[_v] = _u
                if _i == _num_v - 1:
                    _negative_nodes.append(_v)
    _discovered = [False] * (_num_v + 1)
    while _negative_nodes:
        _u = _negative_nodes.popleft()
        _discovered[_u] = True
        _results[_u] = "-"
        for _v in _adjacencies[_u]:
            if not _discovered[_v]:
                _negative_nodes.append(_v)
    return _results


if __name__ == "__main__":
    num_v, num_e = map(int, input().split())
    adjacencies = [[] for _ in range(num_v + 1)]
    edges = []
    for _ in range(num_e):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
        adjacencies[u].append(v)
    start = int(input())
    results = modified_bellman_ford(num_v, edges, adjacencies, start)
    for result in results[1:]:
        if result == float("inf"):
            print("*")
        else:
            print(result)

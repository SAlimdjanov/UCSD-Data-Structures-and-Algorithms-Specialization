""" 
negative_cycle.py

Uses a barebone graph implementation as there currently are issues when using the Graph ADT 
implementation.

TODO: Update solution if Graph ADT implementation is fixed.

"""


def bellman_ford_algorithm(_n, _edges):
    """
    Perform the Bellman-Ford Algorithm to check for a negative cycle in a given graph.

    Args:
        _n (int): Number of vertices
        _edges (list): 2D list containing edges of the form [start, end, weight]

    Returns:
        int: 1 if the graph contains a cycle of negative weight and 0 otherwise.

    """
    _distances = [1001] * (_n + 1)
    _previous = [None] * (_n + 1)
    _distances[1], _negative_nodes = 0, []
    for i in range(_n):
        for _u, _v, _w in _edges:
            if _distances[_v] > _distances[_u] + _w:
                _distances[_v] = _distances[_u] + _w
                _previous[_v] = _u
                if i == _n - 1:
                    _negative_nodes.append(_v)
    if not _negative_nodes:
        return 0
    return 1


if __name__ == "__main__":
    num_v, num_e = map(int, input().split())
    edges = []
    for _ in range(num_e):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    CHECK = bellman_ford_algorithm(num_v, edges)
    print(CHECK)

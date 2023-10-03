# python3

""" 
evacuation.py

Finds the maximum flow in a network to determine how fast people can be evacuated from a 
given city.

"""

from collections import deque


def has_path(_graph, _path):
    """
    Uses BFS and adjacency matrix to check if a path is present.

    Args:
        _graph (list): Adjacency list
        _path (list): Store a constructed path

    Returns:
        bool: True means there is a path, False means there is no path.

    """
    _len_graph = len(_graph)
    _visited = [False] * _len_graph
    _visited[0] = True
    _deque = deque([0])
    while _deque:
        _tmp = _deque.popleft()
        if _tmp == _len_graph - 1:
            return True
        for i in range(_len_graph):
            if not _visited[i] and _graph[_tmp][i] > 0:
                _deque.append(i)
                _visited[i] = True
                _path[i] = _tmp
    return _visited[_len_graph - 1]


def ford_fulkerson(_graph):
    """
    Uses the Ford-Fulkerson algorithm to compute the maximum flow value.

    Args:
        _graph (list): Adjacency matrix

    Returns:
        float: Max flow value

    """
    _flow_val, _len_graph = 0, len(_graph)
    _path = list(range(_len_graph))
    while has_path(_graph, _path):
        _min_flow = float("inf")
        _v = _len_graph - 1
        while _v != 0:
            _u = _path[_v]
            _min_flow = min(_min_flow, _graph[_u][_v])
            _v = _u
        _v = _len_graph - 1
        while _v != 0:
            _u = _path[_v]
            _graph[_u][_v] -= _min_flow
            _graph[_v][_u] += _min_flow
            _v = _u
        _flow_val += _min_flow
    return _flow_val


def read_data():
    """Read input data"""
    num_c, num_e = map(int, input().split())
    _graph = [[0] * num_c for _ in range(num_c)]
    for _ in range(num_e):
        _u, _v, capacity = map(int, input().split())
        _graph[_u - 1][_v - 1] += capacity
    return _graph


if __name__ == "__main__":
    graph = read_data()
    max_flow = ford_fulkerson(graph)
    print(max_flow)

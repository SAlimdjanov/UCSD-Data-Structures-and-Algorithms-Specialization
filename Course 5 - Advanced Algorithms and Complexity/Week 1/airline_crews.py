# python3

""" 
airline_crews.py

Finds the maximum matching in a bipartite graph to assign airline crews to flights in the most 
efficient way.

"""


from collections import deque


def build_network(_f, _c, _bipartite_graph):
    """
    Build a flow network based on the number of flights, crew, and an input bipartite graph.

    Args:
        _f (int): Number of flights
        _c (_type_): Number of crew members
        _bipartite_graph (list): Bipartite graph

    Returns:
        list: Constructed flow network

    """
    _graph = [[0] * (_f + _c + 2) for _ in range(_f + _c + 2)]
    for i in range(1, _f + 1):
        _graph[0][i] = 1
        for j in range(_c):
            _graph[i][_f + 1 + j] = _bipartite_graph[i - 1][j]
    for k in range(_f + 1, _f + _c + 1):
        _graph[k][-1] = 1
    return _graph


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


def max_flow(_graph, _f):
    """
    Solves the maximum bipartite matching problem.

    Args:
        _graph (list): Flow network constructed by a bipartite graph
        _f (int): Number of flights

    Returns:
        list: Each index contains a matched crew member, or -1 if there is no match for that flight.

    """
    _len_graph = len(_graph)
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
    _matches = [-1] * _f
    for i in range(_len_graph):
        if _graph[_len_graph - 1][i] == 1:
            _crew_member = i - _f
            _flight = _graph[i].index(1)
            _matches[_flight - 1] = _crew_member
    return _matches


if __name__ == "__main__":
    num_f, num_c = map(int, input().split())
    bipartite_graph = [list(map(int, input().split())) for _ in range(num_f)]
    network = build_network(num_f, num_c, bipartite_graph)
    matches = max_flow(network, num_f)
    for match in matches:
        print(match, end=" ")

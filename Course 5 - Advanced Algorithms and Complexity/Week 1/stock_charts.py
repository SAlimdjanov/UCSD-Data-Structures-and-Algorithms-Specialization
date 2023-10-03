# python3

""" 
stock_charts.py

Determines the minimum number of overlaid charts needed to show all of the stocks' prices.

"""

from collections import deque


def construct_dag(_s, _stock_data):
    """
    Constructs a Directed Acyclic Graph with stock data.

    Args:
        _s (int): Number of stocks
        _stock_data (list): Stock data

    Returns:
        list: Constructed DAG
    """
    _graph = [[0] * _s for _ in range(_s)]
    for i in range(_s):
        for j in range(i + 1, _s):
            _above = all([x < y for x, y in zip(_stock_data[i], _stock_data[j])])
            _below = all([x > y for x, y in zip(_stock_data[i], _stock_data[j])])
            if _above:
                _graph[i][j] = 1
            elif _below:
                _graph[j][i] = 1
    return _graph


def build_network(_s, _graph):
    """
    Build a flow network based on the number of stocks and input DAG.

    Args:
        _s (int): Number of stocks
        _graph (list): DAG

    Returns:
        list: Constructed flow network

    """
    _network = [[0] * (2 * _s + 2) for _ in range(2 * _s + 2)]
    for i in range(1, _s + 1):
        _network[0][i] = 1
        for j in range(_s):
            _network[i][_s + 1 + j] = _graph[i - 1][j]
    for k in range(_s + 1, 2 * _s + 1):
        _network[k][-1] = 1
    return _network


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
    return _visited[-1]


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


if __name__ == "__main__":
    num_s, num_p = map(int, input().split())
    stock_data = [list(map(int, input().split())) for _ in range(num_s)]
    dag = construct_dag(num_s, stock_data)
    network = build_network(num_s, dag)
    max_flow = ford_fulkerson(network)
    min_num_charts = num_s - max_flow
    print(min_num_charts)

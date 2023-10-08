# python3

""" 
circuit_design.py

Determines how to connect the modules of an integrated circuit with wires so that all the wires 
can be routed on the same layer of the circuit.

"""

# Values for DFS
forward, reverse, non_tree = 1, -1, 0


def read_data():
    """Read and store input data"""
    _n, _m = map(int, input().split())
    _clauses = [list(map(int, input().split())) for _ in range(_m)]
    return _n, _m, _clauses


def obtain_node(i):
    """Obtain node"""
    return 2 * abs(i) - 1 - (i > 0)


def obtain_assignment(k):
    """Obtain assignment"""
    return k // 2 + 1 if 0 == 1 & k else -k // 2


def build_graph(_graph, _graph_rev, _clauses):
    """Construct a graph with input clauses"""
    for _c in _clauses:
        _graph[obtain_node(-_c[0])].append(obtain_node(_c[1]))
        _graph[obtain_node(-_c[1])].append(obtain_node(_c[0]))
        _graph_rev[obtain_node(_c[1])].append(obtain_node(-_c[0]))
        _graph_rev[obtain_node(_c[0])].append(obtain_node(-_c[1]))


def dfs_gen(_graph):
    """DFS generator function that returns a sequence of (start_vertex, end_vertex, edge_type) for a
    given graph"""
    _visited, _len_graph = set(), len(_graph)
    for i in range(_len_graph):
        if i not in _visited:
            yield i, i, forward
            _visited.add(i)
            _stack = [(i, iter(_graph[i]))]
            while _stack:
                _parent, _children = _stack[-1]
                try:
                    _child = next(_children)
                    if _child in _visited:
                        yield _parent, _child, non_tree
                    else:
                        yield _parent, _child, forward
                        _visited.add(_child)
                        _stack.append((_child, iter(_graph[_child])))
                except StopIteration:
                    _stack.pop()
                    if _stack:
                        yield _stack[-1][0], _parent, reverse
            yield i, i, reverse


def dfs_post_order(_graph):
    """Generate all vertices in depth-first dfs_post_order"""
    for _, _w, _edge_type in dfs_gen(_graph):
        if _edge_type is reverse:
            yield _w


def obtain_scc(_graph, _graph_rev):
    """Obtain strongly-connected components"""
    _scc_list, _len_graph = [], len(_graph)
    _post_order = list(dfs_post_order(_graph_rev))
    _reverse_post_order = _post_order[::-1]
    _visited = [False] * _len_graph
    _scc_index, _current_index = [0] * _len_graph, 0
    for _v in _reverse_post_order:
        _scc_set = set()
        if not _visited[_v]:
            _stack = []
            _stack.append(_v)
            while len(_stack) > 0:
                _v = _stack.pop()
                if not _visited[_v]:
                    _visited[_v] = True
                    _scc_set.add(_v)
                    _scc_index[_v] = _current_index
                    for _w in _graph[_v]:
                        _stack.append(_w)
            _scc_list.append(_scc_set)
            _current_index += 1
    return _scc_list, _scc_index


def check_sccs(_scc_list):
    """Validate the list of strongly connected components"""
    for _scc in _scc_list:
        for _v in _scc:
            if obtain_node(-obtain_assignment(_v)) in _scc:
                return False
    return True


def is_satisfiable():
    """Check if input is satisfiable and outputs a solution if it is"""
    _n, _, _clauses = read_data()
    _graph = [[] for _ in range(2 * _n)]
    _graph_rev = [[] for _ in range(2 * _n)]
    _len_graph = len(_graph)
    build_graph(_graph, _graph_rev, _clauses)
    _scc_list, _scc_index = obtain_scc(_graph, _graph_rev)
    if not check_sccs(_scc_list):
        return None
    _result, _assigned = [False] * _n, [False] * _len_graph
    _post_order = dfs_post_order(_graph)
    for _v in _post_order:
        if not _assigned[_v]:
            for _w in _scc_list[_scc_index[_v]]:
                if not _assigned[_w]:
                    _result[abs(obtain_assignment(_w)) - 1] = obtain_assignment(_w) < 0
                    _assigned[_w], _assigned[obtain_node(-obtain_assignment(_w))] = (
                        True,
                        True,
                    )
    return _result, _n


result = is_satisfiable()
if result is None:
    print("UNSATISFIABLE")
else:
    print("SATISFIABLE")
    print(" ".join(str(-i - 1 if result[0][i] else i + 1) for i in range(result[1])))

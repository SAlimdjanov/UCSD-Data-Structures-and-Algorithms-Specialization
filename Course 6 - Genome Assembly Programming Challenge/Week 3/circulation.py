# python3

""" 
circulation.py

Find a circulation if it exists given a network with lower bounds and capacities on edges.

"""

import queue


class Edge:
    """Constructs a graph edge with lower bound and capacity"""

    def __init__(self, start, end, lower_bound, capacity):
        self.start = start
        self.end = end
        self.lower_bound = lower_bound
        self.capacity = capacity
        self.difference = capacity - lower_bound
        self.flow = 0


class FlowGraph:
    """Flow Graph object"""

    def __init__(self, _n):
        self.edges = []
        self._graph = [[] for _ in range(_n + 2)]
        self.vertex_net_demand = [0] * (_n + 2)
        self.graph_total_demand = 0

    def add_edge(self, _start, _end, _lower_bound, _capacity):
        """Add an edge _end the _graph"""
        _fwd_edge = Edge(_start, _end, _lower_bound, _capacity)
        _bw_edge = Edge(_end, _start, 0, 0)
        self._graph[_start].append(len(self.edges))
        self.edges.append(_fwd_edge)
        self._graph[_end].append(len(self.edges))
        self.edges.append(_bw_edge)
        self.vertex_net_demand[_start] += _lower_bound
        self.vertex_net_demand[_end] -= _lower_bound

    def construct_flow(self, _id, _flow):
        """Construct a flow"""
        self.edges[_id].flow += _flow
        self.edges[_id ^ 1].flow -= _flow
        self.edges[_id].difference -= _flow
        self.edges[_id ^ 1].difference += _flow

    def get_ids(self, _start):
        """Get IDs"""
        return self._graph[_start]

    def graph_size(self):
        """Return graph size"""
        return len(self._graph)

    def get_edge(self, _id):
        """Obtain an edge associated with an ID"""
        return self.edges[_id]


class Circulation:
    """Processes and stores input data, then solves the problem"""

    def _read_data(self):
        """Read and process input data accordingly"""
        _num_v, _num_e = map(int, input().split())
        _graph = FlowGraph(_num_v)
        for _ in range(_num_e):
            _start, _end, _lower_bound, _capacity = map(int, input().split())
            _graph.add_edge(_start - 1, _end - 1, _lower_bound, _capacity)
        for _end in range(_num_v):
            if _graph.vertex_net_demand[_end] < 0:
                _graph.add_edge(_num_v, _end, 0, -_graph.vertex_net_demand[_end])
            if _graph.vertex_net_demand[_end] > 0:
                _graph.add_edge(_end, _num_v + 1, 0, _graph.vertex_net_demand[_end])
                _graph.graph_total_demand += _graph.vertex_net_demand[_end]
        return _graph, _num_v, _num_e

    def bfs(self, _graph, _start, _end):
        """Perform Breadth-First search on a graph"""
        _val, _has_path, _size = float("inf"), False, _graph.graph_size()
        _distance, _path, _parent = [float("inf")] * _size, [], [(None, None)] * _size
        _queue = queue.Queue()
        _distance[_start] = 0
        _queue.put(_start)
        while not _queue.empty():
            _curr_start_node = _queue.get()
            for _id in _graph.get_ids(_curr_start_node):
                _curr_edge = _graph.get_edge(_id)
                if (
                    float("inf") == _distance[_curr_edge.end]
                    and _curr_edge.difference > 0
                ):
                    _distance[_curr_edge.end] = _distance[_curr_start_node] + 1
                    _parent[_curr_edge.end] = (_curr_start_node, _id)
                    _queue.put(_curr_edge.end)
                    if _curr_edge.end == _end:
                        while True:
                            _path.insert(0, _id)
                            _curr_val = _graph.get_edge(_id).difference
                            _val = min(_curr_val, _val)
                            if _curr_start_node == _start:
                                break
                            _curr_start_node, _id = _parent[_curr_start_node]
                        _has_path = True
                        return _has_path, _path, _val
        return _has_path, _path, _val

    def max_flow(self, _graph, _start, _end):
        """Finds max flow"""
        _flow = 0
        while True:
            _has_path, _path, _val = self.bfs(_graph, _start, _end)
            if not _has_path:
                return _flow
            for _id in _path:
                _graph.construct_flow(_id, _val)
            _flow += _val

    def find_circulation(self, _graph, _n, _m):
        """Determines if a circulation exists"""
        _flow = self.max_flow(_graph, _n, _n + 1)
        _flows = [0] * _m
        if _flow != _graph.graph_total_demand:
            return False, _flows
        for i in range(_m):
            _fwd_edge = _graph.edges[i * 2]
            _flows[i] = _fwd_edge.flow + _fwd_edge.lower_bound
        return True, _flows

    def __init__(self):
        _graph, _n, _m = self._read_data()
        _flow, _flows = self.find_circulation(_graph, _n, _m)
        self.print_solution(_flow, _flows)

    def print_solution(self, _flow, _flows):
        """Print answer"""
        if not _flow:
            print("NO")
        else:
            print("YES")
            print("\n".join(map(str, _flows)))


if __name__ == "__main__":
    Circulation()

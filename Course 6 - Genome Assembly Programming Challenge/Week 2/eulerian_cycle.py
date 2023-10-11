# python3

""" 
eulerian_cycle.py

Finds a Eulerian cycle in a directed graph or reports that there is none.

"""

import sys


class EulerianCycle:
    """Eulerian Cycle Class"""

    def _input(self):
        """Process input data"""
        _data = list(sys.stdin.read().strip().split())
        self.n, self.unexplored_edges = int(_data[0]), int(_data[1])
        self.adj = [[] for _ in range(self.n)]
        self.outgoing_degree = [0] * self.n
        self.incoming_degree = [0] * self.n
        self.adjacent_to_curr_pos = [0] * self.n
        for i in range(self.unexplored_edges):
            _current_start = int(_data[2 * i + 2]) - 1
            _current_end = int(_data[2 * i + 3]) - 1
            self.adj[_current_start].append(_current_end)
            self.outgoing_degree[_current_start] += 1
            self.incoming_degree[_current_end] += 1
        for i in range(self.n):
            if self.outgoing_degree[i] != self.incoming_degree[i]:
                return False
        return True

    def explore(self, _n):
        """Explores the graph starting from a given node _n"""
        self.path.append(_n)
        _curr_pos = self.adjacent_to_curr_pos[_n]
        _curr_pos_max = self.outgoing_degree[_n]
        while _curr_pos < _curr_pos_max:
            self.adjacent_to_curr_pos[_n] = _curr_pos + 1
            if _curr_pos + 1 < _curr_pos_max:
                self.nodes_of_unused_edges[_n] = len(self.path) - 1
            else:
                if _n in self.nodes_of_unused_edges:
                    del self.nodes_of_unused_edges[_n]
            _v = self.adj[_n][_curr_pos]
            self.path.append(_v)
            _n = _v
            _curr_pos = self.adjacent_to_curr_pos[_n]
            _curr_pos_max = self.outgoing_degree[_n]
            self.unexplored_edges -= 1

    def update_path(self, _start_pos):
        """Update explored path by rotating it so that the path starts from the node _start_pos.
        Updates positions of nodes with unused edges."""
        _l = len(self.path) - 1
        self.path = self.path[_start_pos:_l] + self.path[:_start_pos]
        for node, pos in self.nodes_of_unused_edges.items():
            if pos < _start_pos:
                self.nodes_of_unused_edges[node] = pos + _l - _start_pos
            else:
                self.nodes_of_unused_edges[node] = pos - _start_pos

    def find_eulerian_cycle(self):
        """Finds a Eulerian cycle using Hierholzer's algorithm."""
        self.explore(1)
        while self.unexplored_edges > 0:
            node, pos = self.nodes_of_unused_edges.popitem()
            self.update_path(pos)
            self.explore(node)
        return self.path

    def __init__(self):
        self.unexplored_edges = 0
        self.nodes_of_unused_edges = {}
        self.path = []
        _is_input_balanced = self._input()
        if not _is_input_balanced:
            print("0")
        else:
            print("1")
            self.find_eulerian_cycle()
            self.print_path()

    def print_path(self):
        """Print resulting path"""
        print(" ".join([str(node + 1) for node in self.path[:-1]]))


if __name__ == "__main__":
    EulerianCycle()

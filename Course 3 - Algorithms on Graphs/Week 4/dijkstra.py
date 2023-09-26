""" 
dijkstra.py

Uses a barebone graph implementation with a binary heap as there are outstanding issues when using
the Graph ADT implementation.

TODO: Update solution if Graph ADT implementation is fixed.

"""

from collections import deque


class MinimumCost:
    """Creates an object containing minimum costs for path traversals"""

    def __init__(self, _n, _edges, _start, _end):
        self._edges = _edges
        self._heap = deque()
        for _i in range(_n):
            self._heap.append([_i + 1, float("inf")])
        self._distances = [float("inf")] * (_n + 1)
        self._processed = [False] * (_n + 1)
        self._start = _start
        self._end = _end

    def _sift_down(self, _i):
        """Performs down sifting"""
        _min_index = _i
        _left_child = 2 * _i + 1
        _right_child = 2 * _i + 2
        if (
            _left_child < len(self._heap)
            and self._heap[_left_child][1] < self._heap[_min_index][1]
        ):
            _min_index = _left_child
        if (
            _right_child < len(self._heap)
            and self._heap[_right_child][1] < self._heap[_min_index][1]
        ):
            _min_index = _right_child
        if _min_index != _i:
            self._heap[_i], self._heap[_min_index] = (
                self._heap[_min_index],
                self._heap[_i],
            )
            self._sift_down(_min_index)

    def _sift_up(self, _i):
        """Performs up sifting"""
        while _i > 0 and self._heap[_i][1] < self._heap[(_i - 1) // 2][1]:
            self._heap[_i], self._heap[(_i - 1) // 2] = (
                self._heap[(_i - 1) // 2],
                self._heap[_i],
            )
            _i = (_i - 1) // 2

    def extract_min(self):
        """Remove and return the minimum element"""
        result = self._heap[0]
        self._heap[0] = self._heap[len(self._heap) - 1]
        self._heap.pop()
        self._sift_down(0)
        return result

    def insert(self, _node, _priority):
        """Insert element into the heap"""
        self._heap.append([_node, _priority])
        self._sift_up(len(self._heap) - 1)

    def change_priority(self, _i, _new_priority):
        """Change the priority of an element"""
        self._heap[_i][1] = _new_priority
        self._sift_up(_i)

    def dijkstra_min_cost(self):
        """
        Performs Dijkstra's algorithm to obtain the total cost of traversing a given path.

        Returns:
            int: Minimum cost, -1 if no path can be established.

        """
        self._distances[self._start] = 0
        self.change_priority(self._start - 1, 0)
        while self._heap:
            _u, _ = self.extract_min()
            if not self._processed[_u]:
                self._processed[_u] = True
                for _v, _weight in self._edges[_u]:
                    if self._distances[_v] > self._distances[_u] + _weight:
                        self._distances[_v] = self._distances[_u] + _weight
                        self.insert(_v, self._distances[_v])
        if self._distances[self._end] != float("inf"):
            return self._distances[self._end]
        return -1


if __name__ == "__main__":
    num_v, num_e = map(int, input().split())
    edges = [[] for _ in range(num_v + 1)]
    for _ in range(num_e):
        u, v, w = map(int, input().split())
        edges[u].append((v, w))
    start, end = map(int, input().split())
    flights = MinimumCost(num_v, edges, start, end)
    min_cost = flights.dijkstra_min_cost()
    print(min_cost)

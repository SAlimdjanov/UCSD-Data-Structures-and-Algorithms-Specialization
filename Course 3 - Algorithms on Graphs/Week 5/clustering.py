""" 
clustering.py

Uses barebones implementation, Graph ADT solution still not found.

"""

import math


class ConnectingPoints:
    """Class containing functions to solve the connecting points problem"""

    def __init__(self, _n, _edges, _k):
        self._parent = [i for i in range(_n)]
        self._n = _n
        self._rank = [0] * _n
        self._edges = _edges
        self._k = _k

    def _find(self, _i):
        """Find parent of element _i"""
        if _i != self._parent[_i]:
            self._parent[_i] = self._find(self._parent[_i])
        return self._parent[_i]

    def _union(self, _i, _j):
        """Perform a union of elements _i and _j"""
        i_parent = self._find(_i)
        j_parent = self._find(_j)
        if i_parent == j_parent:
            return
        if self._rank[i_parent] > self._rank[j_parent]:
            self._parent[j_parent] = i_parent
        else:
            self._parent[i_parent] = j_parent
            if self._rank[i_parent] == self._rank[j_parent]:
                self._rank[j_parent] += 1

    def modified_kruskal(self):
        """
        Modified Kruskal's Algorithm to perform the maximum distance instead.

        Returns:
            float: Maximum distance

        """
        _distance = 0
        self._edges.sort(key=lambda x: x[2])
        for _u, _v, _w in self._edges:
            if self._find(_u) != self._find(_v):
                if _distance == self._n - self._k:
                    return _w
                _distance += 1
                self._union(_u, _v)


if __name__ == "__main__":
    num_v = int(input())
    points = [None] * num_v
    edges = []
    for i in range(num_v):
        u, v = map(int, input().split())
        points[i] = (u, v)  # type: ignore
    clusters = int(input())
    for j in range(num_v):
        (x_i, y_i) = points[j]  # type: ignore
        for k in range(j + 1, num_v):
            (x, y) = points[k]  # type: ignore
            distance = math.sqrt((x - x_i) ** 2 + (y - y_i) ** 2)
            edges.append((j, k, distance))
    connecting_points = ConnectingPoints(num_v, edges, clusters)
    maximum_length = connecting_points.modified_kruskal()
    print(f"{maximum_length:.7f}")

""" 
bfs.py

Uses Graph ADT Implementation

"""


class Vertex:
    """Lightweight vertex structure for a graph"""

    __slots__ = ("_element",)

    def __init__(self, _x):
        self._element = _x

    def element(self):
        """Return element associated with this vertex"""
        return self._element

    def __hash__(self):
        """Allows vertex to be map/set key"""
        return hash(id(self))


class Edge:
    """Lightweight edge structure for a graph"""

    __slots__ = ("_origin", "_destination", "_element")

    def __init__(self, _u, _v, _x):
        self._origin = _u
        self._destination = _v
        self._element = _x

    def endpoints(self):
        """Return (u, v) tuple for vertices u and v"""
        return (self._origin, self._destination)

    def opposite(self, _v):
        """Return the vertex that is opposite v on this edge"""
        if _v is self._origin:
            return self._destination
        return self._origin

    def element(self):
        """Return the element associated with this edge"""
        return self._element

    def __hash__(self):
        return hash((self._origin, self._destination))


class Graph:
    """Representation of a simple graph using an adjacency map"""

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """Return True/False if graph is directed/undirected"""
        return bool(self._incoming is not self._outgoing)

    def vertex_count(self):
        """Return the number of vertices in the graph"""
        return len(self._outgoing)

    def vertices(self):
        """Return an iteration of all vertices of the graph"""
        return self._outgoing.keys()

    def edge_count(self):
        """Return the number of edges in the graph"""
        total = sum(len(_e) for _e in self._outgoing.values())
        if self.is_directed():
            return total
        return total // 2

    def edges(self):
        """Return a set of all the edges of the graph"""
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, _u, _v):
        """Return the edge from u to v, or None if not adjacent"""
        return self._outgoing[_u].get(_v)

    def degree(self, _v, outgoing=True):
        """Return number of outgoing edges incident to vertex v in the graph. If the graph is
        directed, optional parameter is used to count incoming edges"""
        if outgoing:
            adj = self._outgoing
        else:
            adj = self._incoming
        return len(adj[_v])

    def incident_edges(self, _v, outgoing=True):
        """Return all outgoing edges incident to vertex v in the graph"""
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[_v].values():
            yield edge

    def insert_vertex(self, _x=None):
        """Insert and return a new Vertex with element x"""
        _v = Vertex(_x)
        self._outgoing[_v] = {}
        if self.is_directed():
            self._incoming[_v] = {}
        return _v

    def insert_edge(self, _u, _v, _x=None):
        """Insert and return a new Edge from u to v with auxiliary element x"""
        _e = Edge(_u, _v, _x)
        self._outgoing[_u][_v] = _e
        self._incoming[_v][_u] = _e


def bfs(_g, _start, _end, discovered):
    """
    Perform a BFS of the undiscovered portion of Graph _g starting at Vertex _start and ending at
    Vertex _end

    Args:
        _g (Graph): Undirected Graph object
        _start (Vertex): Start vertex
        _end (Vertex): End vertex
        discovered (dict): Forest of keys of type Vertex and values of type Edge (the edge used to
                           discover the Vertex)

    Returns:
        bool: True if a path from _start to _end is found, False otherwise
    """
    level = [_start]
    while len(level) > 0:
        next_level = []
        for _u in level:
            for _e in _g.incident_edges(_u):
                _v = _e.opposite(_u)
                if _v not in discovered:
                    discovered[_v] = _e
                    next_level.append(_v)
                    if _v == _end:
                        return True
        level = next_level
    return False


def construct_path(_u, _v, discovered):
    """
    Construct a path from _u to _v. Returns list of vertices of a successfully established path.
    Returns an empty list if no path is possible

    Args:
        _u (Vertex): Start vertex
        _v (Vertex): End vertex
        discovered (dict): Forest of keys of type Vertex and values of type Edge (the edge used to
                           discover the Vertex)

    Returns:
        list: Path vertices if there is a path, empty list if there's no path

    """
    _path = []
    if _v not in discovered:
        return _path
    _path.append(_v)
    walk = _v
    while walk is not _u:
        _e = discovered[walk]
        if _e is None:
            break
        parent = _e.opposite(walk)
        _path.append(parent)
        walk = parent
    _path.reverse()
    if _path[-1].element() != _v.element():
        return []
    return _path if _path[0].element() == _u.element() else []


if __name__ == "__main__":
    g = Graph(directed=False)
    num_v, num_e = map(int, input().split())
    vertices = [g.insert_vertex(i) for i in range(1, num_v + 1)]
    for _ in range(num_e):
        u, v = map(int, input().split())
        g.insert_edge(vertices[u - 1], vertices[v - 1], None)
    start, end = map(int, input().split())
    visited = {}
    if bfs(g, vertices[start - 1], vertices[end - 1], visited):
        path = construct_path(vertices[start - 1], vertices[end - 1], visited)
        if path:
            print(len(path) - 1)
        else:
            print(-1)
    else:
        print(-1)

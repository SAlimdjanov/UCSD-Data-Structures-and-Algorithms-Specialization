""" 
connected_components.py

"""


def explore(adj, visit, vertex):
    """
    Explore edges in depth-first order

    Args:
        adj (list): List of adjacent edges
        visit (list): List of bools indicating whether a vertex was visited
        vertex (int): Vertex

    """
    visit[vertex] = True
    for elem in adj[vertex]:
        if not visit[elem]:
            explore(adj, visit, elem)


def connected_components(num_vertices, adj, visit):
    """
    Obtain the number of connected components

    Args:
        num_vertices (int): Number of vertices
        adj (list): List of adjacent edges
        visit (list): List of bools indicating whether a vertex was visited

    Returns:
        int: Number of connected components

    """
    num_cc = 0
    for elem in range(1, num_vertices + 1):
        if not visit[elem]:
            explore(adj, visit, elem)
            num_cc += 1
    return num_cc


if __name__ == "__main__":
    num_v, num_e = map(int, input().split())
    edges, adjacencies = [], [[] for _ in range(num_v + 1)]
    for _ in range(num_e):
        edges.append(tuple(map(int, input().split())))
    for i, j in edges:
        adjacencies[i].append(j)
        adjacencies[j].append(i)
    visited = [False] * (num_v + 1)
    CC = connected_components(num_v, adjacencies, visited)
    print(CC)

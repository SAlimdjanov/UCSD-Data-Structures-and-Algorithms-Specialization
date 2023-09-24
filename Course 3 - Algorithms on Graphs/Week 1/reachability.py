""" 
reachability.py

"""


def explore(adj, visit, v_1, v_2):
    """
    Explore edges in depth-first order

    Args:
        adj (list): List of adjacent edges
        visit (list): List of bools indicating whether a vertex was visited
        v_1 (int): First edge endpoint (vertex 1)
        v_2 (int): Second edge endpoint (vertex 2)

    """
    visit[v_1] = True
    for v_prime in adj[v_1]:
        if not visited[v_prime]:
            explore(adj, visited, v_prime, v_2)


if __name__ == "__main__":
    num_v, num_e = map(int, input().split())
    edges, adjacencies = [], [[] for _ in range(num_v + 1)]
    for _ in range(num_e):
        edges.append(tuple(map(int, input().split())))
    for i, j in edges:
        adjacencies[i].append(j)
        adjacencies[j].append(i)
    u, v = map(int, input().split())
    visited = [False] * (num_v + 1)
    explore(adjacencies, visited, u, v)
    if visited[v]:
        print(1)
    else:
        print(0)

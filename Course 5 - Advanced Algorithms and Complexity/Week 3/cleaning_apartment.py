# python3

""" 
cleaning_apartment.py

"""

import itertools


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
clauses, positions = [], range(1, n + 1)
adjacencies = [[] for _ in range(n)]
for u, v in edges:
    adjacencies[u - 1].append(v - 1)
    adjacencies[v - 1].append(u - 1)


def print_equisatisfiable_sat_formula():
    """Prints an equisatisfiable formula for the SAT solver"""

    def varnum(i, j):
        """Compute numerical value for inputs"""
        return n * i + j

    def exactly_one_of(literals):
        """Construct a set of clauses for the SAT problem"""
        clauses.append(list(literals))
        for pair in itertools.combinations(literals, 2):
            clauses.append([-l for l in pair])

    for i in range(n):
        exactly_one_of([varnum(i, position) for position in positions])

    for j in positions:
        exactly_one_of([varnum(i, j) for i in range(n)])

    for j in positions[:-1]:
        for i, nodes in enumerate(adjacencies):
            clauses.append([-varnum(i, j)] + [varnum(node, j + 1) for node in nodes])

    print(len(clauses), n * n)
    for clause in clauses:
        clause.append(0)
        print(" ".join(map(str, clause)))


print_equisatisfiable_sat_formula()

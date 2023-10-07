# python3

""" 
gsm_network.py

"""

import itertools


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
clauses, colours = [], range(1, 4)


def print_equisatisfiable_sat_formula():
    """Prints an equisatisfiable formula for the SAT solver"""

    def varnum(i, colour):
        """Compute numerical value for inputs"""
        # The following assertion from sudoku_solver.py caused the program
        # assert i in colours and colour in colours
        return 3 * (i - 1) + colour

    def exactly_one_of(literals):
        """Construct a set of clauses for the SAT problem"""
        literals = [varnum(literals, colour) for colour in colours]
        clauses.append(list(literals))
        for pair in itertools.combinations(literals, 2):
            clauses.append([-l for l in pair])

    def encode_adjacencies(i, j):
        """Encodes adjacency constraints for each i and j"""
        for colour in colours:
            clauses.append([-varnum(i, colour), -varnum(j, colour)])

    for i in range(1, n + 1):
        exactly_one_of(i)

    for i, j in edges:
        encode_adjacencies(i, j)

    print(len(clauses), n * 3)
    for clause in clauses:
        clause.append(0)
        print(" ".join(map(str, clause)))


print_equisatisfiable_sat_formula()

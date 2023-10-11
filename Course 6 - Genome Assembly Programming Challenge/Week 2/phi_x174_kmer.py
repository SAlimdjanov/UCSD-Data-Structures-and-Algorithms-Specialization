# python3

""" 
phi_x174_kmer.py

Performs genome assembly and return the circular genome from which the k-mers came from, given a 
k-mer composition of some unknown string.

"""

from collections import defaultdict


def traverse_adjacencies(_reads, _adjacencies):
    """Traverses a graph represented by an adjacency list to find cycles that cover all nodes in
    the data _reads"""
    _already_visited = set()
    _path = [_reads[0][:-1]]
    while len(_already_visited) < len(_reads):
        i, _new_cycle = 0, 0
        for i, _node in enumerate(_path):
            _all_visited = True
            for _next_node in _adjacencies[_node]:
                if _next_node[1] not in _already_visited:
                    _all_visited = False
                    break
            if _all_visited:
                continue
            _new_cycle = [_node]
            current = _node
            find_next_node = True
            while find_next_node:
                find_next_node = False
                for _next_node in _adjacencies[current]:
                    if _next_node[1] not in _already_visited:
                        _already_visited.add(_next_node[1])
                        _new_cycle.append(_next_node[0])
                        current = _next_node[0]
                        find_next_node = True
                        break
            break
        _path = _path[:i] + _new_cycle + _path[i + 1 :]  # type: ignore
    return _path


if __name__ == "__main__":
    DEFAULT_READ = 5396
    reads_list = []
    for _ in range(DEFAULT_READ):
        reads_list.append(input())
    adjacencies = defaultdict(list)
    ID = 0
    for read in reads_list:
        adjacencies[read[:-1]].append((read[1:], ID))
        ID += 1
    path = traverse_adjacencies(reads_list, adjacencies)
    CYCLE = ""
    for node in path:
        CYCLE += node[0]
    print(CYCLE[:-1])

# python3

""" 
optimal_kmer_size.py

Given a list of error-free reads, return an integer k such that, when a de Bruijn graph is created 
from the k-length fragments of the reads, the de Bruijn graph has a single possible Eulerian Cycle.

"""

import sys

NUM_READS = 1618


def optimal_kmers(_num, _reads):
    """Checks if it is possible to find a series of overlapping k-mers from the input reads"""
    _kmers = set()
    for _read in _reads:
        for i in range(0, len(_read) - _num + 1):
            _kmers.add(_read[i : i + _num])
    _prefixes, _suffixes = set(), set()
    for kmer in _kmers:
        _prefixes.add(kmer[:-1])
        _suffixes.add(kmer[1:])
    return _prefixes == _suffixes


if __name__ == "__main__":
    reads = []
    for _ in range(NUM_READS):
        read = sys.stdin.readline().strip()
        reads.append(read)
    for n in range(len(reads[2]), 1, -1):
        if optimal_kmers(n, reads):
            print(n)
            break

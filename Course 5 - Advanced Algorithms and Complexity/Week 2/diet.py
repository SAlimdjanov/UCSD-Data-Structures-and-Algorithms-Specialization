# python3

""" 
diet.py

Solves the Optimal Diet problem.

"""

import sys
import itertools
import copy

EPS = 1e-5
MAX_AMOUNT = int(1e9)  # Infinity placeholder


class Position:
    """Creates a position object"""

    def __init__(self, row, column):
        self.row = row
        self.column = column


def select_pivot(_pivot_element, _a, _used_rows):
    """Select pivot element"""
    while _pivot_element.row < len(_a) and (
        _used_rows[_pivot_element.row]
        or _a[_pivot_element.row][_pivot_element.column] == 0
    ):
        _pivot_element.row += 1
    if _pivot_element.row == len(_a):
        return False
    else:
        return _pivot_element


def swap_lines(_a, _b, _used_rows, _pivot_element):
    """Swaps a row with the pivot element to be above rows without the pivot element"""
    _a[_pivot_element.column], _a[_pivot_element.row] = (
        _a[_pivot_element.row],
        _a[_pivot_element.column],
    )
    _b[_pivot_element.column], _b[_pivot_element.row] = (
        _b[_pivot_element.row],
        _b[_pivot_element.column],
    )
    _used_rows[_pivot_element.column], _used_rows[_pivot_element.row] = (
        _used_rows[_pivot_element.row],
        _used_rows[_pivot_element.column],
    )
    _pivot_element.row = _pivot_element.column


def process_pivot(_a, _b, _pivot_element, _used_rows):
    """Process the pivot element"""
    _len_a = len(_a)
    _scale = _a[_pivot_element.row][_pivot_element.column]
    if _scale != 1:
        for _i in range(_len_a):
            _a[_pivot_element.row][_i] /= _scale
        _b[_pivot_element.row] /= _scale
    for _i in range(_len_a):
        if _i != _pivot_element.row:
            _factor = _a[_i][_pivot_element.column]
            for j in range(_len_a):
                _a[_i][j] -= _a[_pivot_element.row][j] * _factor
            _b[_i] -= _b[_pivot_element.row] * _factor
    _used_rows[_pivot_element.row] = True


def find_subsets(_num_e, _num_v):
    """Find subsets present in input data"""
    _list = list(range(_num_e + _num_v + 1))
    _subsets = list(map(set, itertools.combinations(_list, _num_v)))
    return _subsets


def solve_eq(_subset, _m_a, _m_b):
    """Solves an input Equation object with Gaussian elimination"""
    _a, _b = [], []
    for _i in _subset:
        _a.append(copy.deepcopy(_m_a[_i]))
        _b.append(copy.deepcopy(_m_b[_i]))
    size = len(_a)
    used_rows = [False] * size
    for _i in range(size):
        pivot = Position(0, _i)
        pivot = select_pivot(pivot, _a, used_rows)
        if not pivot:
            return None
        swap_lines(_a, _b, used_rows, pivot)
        process_pivot(_a, _b, pivot, used_rows)
    return _b


def check_solution(_solution, _m_a, _m_b, _num_v):
    """Check the obtained solution"""
    _len_a = len(_m_a)
    for _i in range(_len_a):
        _total = 0
        for j in range(_num_v):
            _total += _m_a[_i][j] * _solution[j]
        if _total - _m_b[_i] > EPS:
            return False
    return True


def solve(_subsets, _m_a, _m_b, _pleasure, _num_v):
    """Solve with gaussian elimination"""
    _solutions = []
    for _subset in _subsets:
        _solution = solve_eq(_subset, _m_a, _m_b)
        if _solution is not None:
            if check_solution(_solution, _m_a, _m_b, _num_v):
                _solutions.append(_solution)
    if len(_solutions) == 0:
        print("No solution")
    else:
        _best = float("-inf")
        _result = None
        for _s in _solutions:
            _p = 0
            for _i in range(_num_v):
                _p += _pleasure[_i] * _s[_i]
            if _p > _best:
                _best = _p
                _result = _s
        _amount = 0
        if _result is not None:
            for _r in _result:
                _amount += _r
        if _amount > MAX_AMOUNT:
            print("Infinity")
        else:
            print("Bounded solution")
            if _result is not None:
                for _r in _result:
                    print("{0:.15f}".format(_r), end=" ")


if __name__ == "__main__":
    num_e, num_v = map(int, input().split())
    a = []
    for i in range(num_e):
        a.append(list(map(int, input().split())))
    b = list(map(int, input().split()))
    pleasure_list = list(map(int, input().split()))
    for i in range(num_v):
        ipt_list = [0] * num_v
        ipt_list[i] = -1
        a.append(ipt_list)
        b.append(0)
    a.append([1] * num_v)
    b.append(MAX_AMOUNT + 1)
    subsets = find_subsets(num_e, num_v)
    solve(subsets, a, b, pleasure_list, num_v)
    sys.exit(0)

# python3

""" 
energy_values.py

Solves the linear equation Ax = b for x.

"""


import sys


class Equation:
    """Creates an equation object where (m_a)x = (m_b)"""

    def __init__(self, m_a, m_b):
        self.m_a = m_a
        self.m_b = m_b


class Position:
    """Creates a matrix position object"""

    def __init__(self, row, column):
        self.row = row
        self.column = column


def read_data():
    """Read input data and store accordingly"""
    _size = int(input())
    _a, _b = [], []
    for _ in range(_size):
        _line = list(map(float, input().split()))
        _a.append(_line[:_size])
        _b.append(_line[_size])
    return Equation(_a, _b)


def select_pivot(_pivot_element, _a, _used_rows):
    """Select pivot element"""
    while (
        _used_rows[_pivot_element.row]
        or _a[_pivot_element.row][_pivot_element.column] == 0
    ):
        _pivot_element.row += 1
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
        for i in range(_len_a):
            _a[_pivot_element.row][i] /= _scale
        _b[_pivot_element.row] /= _scale
    for i in range(_len_a):
        if i != _pivot_element.row:
            _factor = _a[i][_pivot_element.column]
            for j in range(_len_a):
                _a[i][j] -= _a[_pivot_element.row][j] * _factor
            _b[i] -= _b[_pivot_element.row] * _factor
    _used_rows[_pivot_element.row] = True


def solve_equation(_equation):
    """Solves an input Equation object with Gaussian elimination"""
    _a = _equation.m_a
    _b = _equation.m_b
    _size = len(_a)
    _used_rows = [False] * _size
    for i in range(_size):
        _pivot_element = Position(0, i)
        _pivot_element = select_pivot(_pivot_element, _a, _used_rows)
        swap_lines(_a, _b, _used_rows, _pivot_element)
        process_pivot(_a, _b, _pivot_element, _used_rows)
    return _b


def print_column(_column):
    """Print a column"""
    _size = len(_column)
    for row in range(_size):
        print("%.8lf" % _column[row], end=" ")


if __name__ == "__main__":
    equation = read_data()
    x = solve_equation(equation)
    print_column(x)
    sys.exit(0)

""" 
a_plus_b.py

Returns the sum of two integers.

"""

def sum_of_digits(num1, num2):
    """Add a + b"""
    return num1 + num2

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_digits(a, b))

""" 
a_plus_b.py

Returns the sum of two integers. Test program for the grading system.

"""


def sum_of_digits(num1, num2):
    """
    Adds two digits

    Args:
        num1 (int): Integer A
        num2 (int): Integer B

    Returns:
        int: Sum of A + B

    """
    return num1 + num2


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(sum_of_digits(a, b))

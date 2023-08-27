""" 
greatest_common_dividers.py

"""


def greatest_common_divisor(num_a, num_b):
    """Obtains GCD"""
    if b == 0:
        return num_a
    while num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_a


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(greatest_common_divisor(a, b))

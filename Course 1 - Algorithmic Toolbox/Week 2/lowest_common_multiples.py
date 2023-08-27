""" 
lowest_common_multiples.py

"""


def greatest_common_divisor(num_a, num_b):
    """Obtains GCD"""
    if b == 0:
        return num_a
    while num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_a


def lowest_common_multiple(num_a, num_b):
    """Obtains LCM"""
    return (num_a * num_b) // greatest_common_divisor(num_a, num_b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lowest_common_multiple(a, b))

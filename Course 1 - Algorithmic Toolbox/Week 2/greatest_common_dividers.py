""" 
greatest_common_dividers.py

"""


def greatest_common_divisor(num_a, num_b):
    """
    Obtains the greatest common divisor for two given integers

    Args:
        num_a (int): Integer a
        num_b (int): Integer b

    Returns:
        int: Greatest common divisor

    """
    if b == 0:
        return num_a

    while num_b:
        num_a, num_b = num_b, num_a % num_b

    return num_a


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(greatest_common_divisor(a, b))

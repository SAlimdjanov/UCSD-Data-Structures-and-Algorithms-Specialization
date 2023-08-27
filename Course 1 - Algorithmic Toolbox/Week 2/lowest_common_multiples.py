""" 
lowest_common_multiples.py

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


def lowest_common_multiple(num_a, num_b):
    """
    Obtains the lowest common multiple for two given integers using the
    greatest_common_divisor function

    Args:
        num_a (int): Integer a
        num_b (int): Integer b

    Returns:
        int: Lowest common multiple

    """
    return (num_a * num_b) // greatest_common_divisor(num_a, num_b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lowest_common_multiple(a, b))

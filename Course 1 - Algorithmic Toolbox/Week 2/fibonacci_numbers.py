""" 
fibonacci_numbers.py

"""


def fibonacci_numbers(num):
    """
    Compute the last number in a Fibonacci sequence

    Args:
        num (int): Integer n where F_n is the n-th Fibonacci number

    Returns:
        int: F_n - the n-th number in the sequence

    """
    if num == 0:
        return num

    if 1 <= num <= 45:
        numbers_list = [None] * (num + 1)
        numbers_list[0] = 0
        numbers_list[1] = 1

        for i in range(2, num + 1):
            numbers_list[i] = numbers_list[i - 1] + numbers_list[i - 2]

        return numbers_list[num]

    return None


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_numbers(n))

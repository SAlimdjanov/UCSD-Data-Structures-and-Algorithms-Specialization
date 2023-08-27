""" 
last_digit_of_fibonacci_number.py

"""


def last_digit_of_fibonacci_number(num):
    """
    Obtain the last digit of the n-th number in a Fibonacci sequence

    Args:
        num (int): Integer n

    Returns:
        int: The last digit of F_n

    """
    pisano_period = 60  # modulo 10 pisano period is 60

    if num <= 1:
        return n

    if 2 <= num <= 10**6:
        # Only keep the last two numbers computed in the sequence for memory conservation
        last_two_nums = [0, 1]

        for i in range(2, pisano_period):
            last_two_nums.append((last_two_nums[i - 1] + last_two_nums[i - 2]) % 10)

        return last_two_nums[num % pisano_period]

    return None


if __name__ == "__main__":
    n = int(input())
    print(last_digit_of_fibonacci_number(n))

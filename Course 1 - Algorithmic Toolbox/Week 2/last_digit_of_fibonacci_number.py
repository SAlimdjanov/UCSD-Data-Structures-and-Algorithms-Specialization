""" 
last_digit_of_fibonacci_number.py

"""


def last_digit_of_fibonacci_number(num):
    """Computes the last digit of the last number in a Fibonacci sequence"""
    pisano_period = 60  # modulo 10 pisano period is 60
    if num <= 1:
        return n
    if 2 <= num <= 10**6:
        last_two_nums = [0, 1]
        for i in range(2, pisano_period):
            last_two_nums.append((last_two_nums[i - 1] + last_two_nums[i - 2]) % 10)
        return last_two_nums[num % pisano_period]
    return None


if __name__ == "__main__":
    n = int(input())
    print(last_digit_of_fibonacci_number(n))

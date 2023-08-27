"""
Maximum-Pairwise-Product.py

Takes a two line input of the form:

Integer n
n number of non-negative integers

Example:

3
2 4 6

Outputs the maximum product of the two largest numbers in the set.

Example output:

24

"""

def max_pairwise_product(numbers):
    """Computes maximum pairwise product"""
    max_1 = max(numbers)
    numbers.remove(max_1)
    max_2 = max(numbers)
    return max_1 * max_2

if __name__ == '__main__':
    n = int(input())
    input_nums = list(map(int, input().split()))
    print(max_pairwise_product(input_nums))

"""
maximum-pairwise-product.py


"""


def max_pairwise_product(numbers):
    """
    Find the maximum pairwise product of a set of numbers

    Args:
        numbers (int list): list of integers

    Returns:
        int: Maximum pairwise product

    """
    max_1 = max(numbers)
    numbers.remove(max_1)
    max_2 = max(numbers)

    return max_1 * max_2


if __name__ == "__main__":
    n = int(input())
    input_nums = list(map(int, input().split()))
    print(max_pairwise_product(input_nums))

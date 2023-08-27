""" 
majority_element.py

"""


def majority_element(nums_list):
    """
    Determines if there is a majority element in a list of numbers

    Args:
        nums_list (int list): list of n integers

    Returns:
        int: Returns 1 if an element is found more than n/2 times, 0 if not.

    """
    value, count = None, 0

    for number in nums_list:
        if count == 0:
            value = number
            count = 1
        elif value == number:
            count += 1
        else:
            count -= 1

    count = nums_list.count(value)

    if count > len(nums_list) // 2:
        return 1

    return 0


if __name__ == "__main__":
    _ = int(input())
    a = list(map(int, input().split()))
    print(majority_element(a))

""" 
majority_element.py

"""


def majority_element(nums_list):
    """Finds the majority element"""
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

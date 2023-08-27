""" 
binary_search_duplicates.py

"""


def binary_search_duplicates(nums_list, queries):
    """Solves the Binary search duplicates problem with the iterative version"""
    results_list = []
    for key in queries:
        low, high = 0, len(nums_list) - 1
        key_index = -1
        while low <= high:
            mid = low + (high - low) // 2
            if key == nums_list[mid]:
                key_index = mid
                high = mid - 1
            elif key < nums_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
        results_list.append(key_index)
    return results_list


if __name__ == "__main__":
    _ = int(input())
    k = list(map(int, input().split()))
    _ = int(input())
    q = list(map(int, input().split()))
    print(" ".join(map(str, binary_search_duplicates(k, q))))

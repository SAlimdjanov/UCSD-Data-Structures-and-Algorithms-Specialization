""" 
binary-search.py

"""


def binary_search(nums_list, queries):
    """
    Solves the 'Sorted Array Multiple Search Problem' with the iterative version

    Args:
        nums_list (int list): List of numbers
        queries (int list): List of query numbers

    Returns:
        int list: list of numbers containing the results of the query. If the query is not found,
        -1 is appended.

    """
    results_list = []

    for key in queries:
        low, high = 0, len(nums_list) - 1
        result = -1

        while low <= high:
            mid = low + (high - low) // 2
            if key == nums_list[mid]:
                result = mid
                break
            if key < nums_list[mid]:
                high = mid - 1
            else:
                low = mid + 1

        results_list.append(result)

    return results_list


if __name__ == "__main__":
    _ = int(input())
    k = list(map(int, input().split()))
    _ = int(input())
    q = list(map(int, input().split()))
    print(" ".join(map(str, binary_search(k, q))))

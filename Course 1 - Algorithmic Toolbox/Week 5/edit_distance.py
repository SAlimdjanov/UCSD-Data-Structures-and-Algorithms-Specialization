""" 
edit_distance.py

"""


def edit_distance(first_string, second_string):
    """
    Solves the edit distance problem with dynamic programming

    Args:
        first_string (str): String #1
        second_string (str): String #2

    Returns:
        int: The minimum number of single-symbol insertions, deletions, and substitutions to
        transform one string into the other one.

    """
    len1, len2 = len(first_string), len(second_string)

    # Create 2D matrix to store results
    matrix = [[float("inf")] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        matrix[i][0] = i

    for j in range(len2 + 1):
        matrix[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            diff = 0 if first_string[i - 1] == second_string[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + diff
            )

    return matrix[len1][len2]


if __name__ == "__main__":
    print(edit_distance(input(), input()))

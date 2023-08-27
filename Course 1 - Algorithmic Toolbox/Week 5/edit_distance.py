""" 
edit_distance.py

"""


def edit_distance(first_string, second_string):
    """Edit distance dynamic programming"""
    len1, len2 = len(first_string), len(second_string)
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

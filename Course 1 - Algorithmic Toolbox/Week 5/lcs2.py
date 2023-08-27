""" 
lcs2.py

"""


def lcs2(first_sequence, second_sequence):
    """
    Compute the length of the longest common subsequence of two sequences

    Args:
        first_sequence (int list): First sequence of length n
        second_sequence (int list): Second sequence of length m

    Returns:
        int : maximum length of a common subsequence. If no such subsequence exists, 0 is returned.

    """
    len1 = len(first_sequence)
    len2 = len(second_sequence)

    # 2D Array to store results
    subsequence = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Iterate through the array and populate the results
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if first_sequence[i - 1] == second_sequence[j - 1]:
                subsequence[i][j] = subsequence[i - 1][j - 1] + 1
            else:
                subsequence[i][j] = max(subsequence[i - 1][j], subsequence[i][j - 1])

    # Return the answer, located in subsequence matrix S[n][m]
    return subsequence[len1][len2]


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))

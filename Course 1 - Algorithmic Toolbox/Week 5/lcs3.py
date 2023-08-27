"""
lcs3.py

"""


def lcs3(first_sequence, second_sequence, third_sequence):
    """
    Compute the length of the longest common subsequence of three sequences

    Args:
        first_sequence (int list): First sequence of length n
        second_sequence (int list): Second sequence of length m
        third_sequence (int list): Third sequence of length q

    Returns:
        int : maximum length of a common subsequence. If no such subsequence exists, 0 is returned.

    """
    len1, len2, len3 = len(first_sequence), len(second_sequence), len(third_sequence)

    # Create 3D array to store results
    subsequence = [[[0] * (len3 + 1) for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    # Iterate through each dimension of the array and populate the results
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            for k in range(1, len3 + 1):
                if (
                    first_sequence[i - 1]
                    == second_sequence[j - 1]
                    == third_sequence[k - 1]
                ):
                    subsequence[i][j][k] = subsequence[i - 1][j - 1][k - 1] + 1
                else:
                    subsequence[i][j][k] = max(
                        subsequence[i - 1][j][k],
                        subsequence[i][j - 1][k],
                        subsequence[i][j][k - 1],
                    )

    # Return S[n][m][q] which is the maximum value
    return subsequence[len1][len2][len3]


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n
    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m
    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q
    print(lcs3(a, b, c))

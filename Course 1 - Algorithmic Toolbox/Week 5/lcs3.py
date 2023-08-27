"""
lcs3.py

"""


def lcs3(first_sequence, second_sequence, third_sequence):
    """Compute the longest common subsequence of three sequences"""
    len1, len2, len3 = len(first_sequence), len(second_sequence), len(third_sequence)
    subsequence = [[[0] * (len3 + 1) for _ in range(len2 + 1)] for _ in range(len1 + 1)]
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

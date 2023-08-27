""" 
lcs2.py

"""


def lcs2(first_sequence, second_sequence):
    """Compute longest common subsequence of two sequences"""
    len1 = len(first_sequence)
    len2 = len(second_sequence)
    subsequence = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if first_sequence[i - 1] == second_sequence[j - 1]:
                subsequence[i][j] = subsequence[i - 1][j - 1] + 1
            else:
                subsequence[i][j] = max(subsequence[i - 1][j], subsequence[i][j - 1])
    return subsequence[len1][len2]


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))

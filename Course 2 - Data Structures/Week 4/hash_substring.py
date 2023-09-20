"""
hash_substring.py

"""

import random


def read_input():
    """
    Read input strings

    Returns:
        str: Input string

    """
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    """
    Print output

    Args:
        output (str): Output string

    """
    print(" ".join(map(str, output)))


def poly_hash(str_s, prime_p, x_val):
    """
    Polynomial Hashing

    Args:
        str_s (str): String S
        prime_p (int): Large prime number p
        x_val (int): x value

    Returns:
        int: hash value

    """
    hash_val, len_str_s = 0, len(str_s)
    for i in range(len_str_s - 1, -1, -1):
        hash_val = (hash_val * x_val + ord(str_s[i])) % prime_p
    return hash_val


def precompute_hashes(str_t, len_str_p, prime_p, x_val):
    """
    Precompute hash values

    Args:
        str_t (str): String T
        len_str_p (int): Length of String P
        prime_p (int): Large prime number p
        x_val (int): x value

    Returns:
        list: Hash values

    """
    len_str_t = len(str_t)
    substring = str_t[len_str_t - len_str_p :]
    hashes = list([] for _ in range(len_str_t - len_str_p + 1))
    hashes[len_str_t - len_str_p] = poly_hash(substring, prime_p, x_val)  # type: ignore
    y_val = 1
    for i in range(1, len_str_p + 1):
        y_val = (y_val * x_val) % prime_p
    for i in range(len_str_t - len_str_p - 1, -1, -1):
        hashes[i] = (
            x_val * hashes[i + 1] + ord(str_t[i]) - y_val * ord(str_t[i + len_str_p])
        ) % prime_p
    return hashes


def rabin_karp(str_t, str_p):
    """
    Rabin-Karp Algorithm for searching substrings

    Args:
        str_t (str): Text string T
        str_p (str): Phrase/Word string P

    Returns:
        list: All positions in T between 0 and len(T) - len(P) such that T[i...(i + len(P) - 1)] = P

    """
    len_str_t, len_str_p = len(str_t), len(str_p)
    prime_p = 100000007  # Prime value greater than 10^8, the max length of all occurences P in T
    x_val = random.randint(1, prime_p - 1)
    positions = []
    p_hash = poly_hash(str_p, prime_p, x_val)
    hashes = precompute_hashes(str_t, len_str_p, prime_p, x_val)
    for i in range(0, len_str_t - len_str_p + 1):
        if p_hash == hashes[i]:
            positions.append(i)
    return positions


if __name__ == "__main__":
    pattern_string = input()
    text_string = input()
    result = rabin_karp(text_string, pattern_string)
    for position in result:
        print(position, end=" ")

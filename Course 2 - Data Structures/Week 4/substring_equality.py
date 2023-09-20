"""
substring_equality.py

"""

import random


class Solver:
    """
    Solver class for the substring equality problem

    """

    def __init__(self, string):
        self.string = string

    def precompute_hashes(self, str_s, prime_p, x_val):
        """
        Precompute hash values

        Args:
            str_s (str): String S
            prime_p (int): Large prime number p
            x_val (int): x value

        Returns:
            list: Hash values

        """
        len_str_s = len(str_s)
        hashes = list([] for _ in range(len_str_s + 1))
        hashes[0] = 0  # type: ignore
        for i in range(1, len_str_s + 1):
            hashes[i] = (hashes[i - 1] * x_val + ord(str_s[i - 1])) % prime_p
        return hashes

    def hash_value(self, hash_table, prime_p, x_val, start_val, length):
        """
        Hash Function

        Args:
            str_s (str): String S
            prime_p (int): Large prime number p
            x_val (int): x value

        Returns:
            int: hash value

        """
        y_val = pow(x_val, length, prime_p)
        hash_value = (
            hash_table[start_val + length] - y_val * hash_table[start_val]
        ) % prime_p
        return hash_value

    def substring_equality(
        self, hashes_1, hashes_2, prime_1, prime_2, x_val, q_a, q_b, q_l
    ):
        """
        Check for substring equality

        Args:
            hashes_1 (list): First set of precomputed hashes
            hashes_2 (list): Second set of precomputed hashes
            prime_1 (int): First large prime value
            prime_2 (int): Second large prime value
            x_val (int): x value (multiplier)
            q_a (int): Query integer a
            q_b (int): Query integer b
            q_l (int): Query integer l

        Returns:
            str: "Yes" or "No"

        """
        s1_hash_1 = self.hash_value(hashes_1, prime_1, x_val, q_a, q_l)
        s1_hash_2 = self.hash_value(hashes_2, prime_2, x_val, q_a, q_l)
        s2_hash_1 = self.hash_value(hashes_1, prime_1, x_val, q_b, q_l)
        s2_hash_2 = self.hash_value(hashes_2, prime_2, x_val, q_b, q_l)
        if s1_hash_1 == s2_hash_1 and s1_hash_2 == s2_hash_2:
            return "Yes"
        return "No"


if __name__ == "__main__":
    string_s = input()
    q = int(input())
    solver = Solver(string_s)
    m1, m2 = 1000000007, 1000000009
    x = random.randint(1, m1)
    hash_1 = solver.precompute_hashes(string_s, m1, x)
    hash_2 = solver.precompute_hashes(string_s, m2, x)
    for j in range(q):
        a, b, l = map(int, input().split())
        print(solver.substring_equality(hash_1, hash_2, m1, m2, x, a, b, l))

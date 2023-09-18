"""
hash_chains.py

"""

from collections import deque


class Query:
    """
    Creates a query object

    """

    def __init__(self, query):
        self.type = query[0]
        if self.type == "check":
            self.index = int(query[1])
        else:
            self.string = query[1]


class PolynomialHash:
    """Creates a Polynomial Hash Object"""

    x_val = 263
    prime_p = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elements = list(deque() for _ in range(self.bucket_count))

    def poly_hash(self, string):
        """
        Polynomial Hashing

        Args:
            string (str): Input string

        Returns:
            int: Hash function value given the input string

        """
        hash_val = 0
        for char in reversed(string):
            hash_val = (hash_val * self.x_val + ord(char)) % self.prime_p
        return hash_val % self.bucket_count

    def process_query(self, query):
        """
        Processes an incoming query

        Args:
            query (Query): Query object

        """
        if query.type == "check":
            if self.elements[query.index]:
                print(" ".join(self.elements[query.index]))
            else:
                print()
        else:
            hash_value = self.poly_hash(query.string)
            if query.type == "add":
                if query.string not in self.elements[hash_value]:
                    self.elements[hash_value].appendleft(query.string)
            elif query.type == "del":
                if query.string in self.elements[hash_value]:
                    self.elements[hash_value].remove(query.string)
            elif query.type == "find":
                if query.string in self.elements[hash_value]:
                    print("yes")
                else:
                    print("no")


if __name__ == "__main__":
    n_buckets = int(input())
    hash_table = PolynomialHash(n_buckets)
    n_queries = int(input())
    for _ in range(n_queries):
        command = Query(input().split())
        hash_table.process_query(command)

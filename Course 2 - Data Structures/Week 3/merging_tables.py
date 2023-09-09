# python3


class Database:
    """
    Creates a Database object

    """

    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [0] * n_tables
        self.parents = list(range(n_tables))

    def find_parent(self, index):
        """
        Find the value of the parent node given the index of a child node and compress path.

        Args:
            index (int): Index of a child node

        Returns:
            int: Value of the parent node

        """
        if index != self.parents[index]:
            self.parents[index] = self.find_parent(self.parents[index])
        return self.parents[index]

    def merge(self, src, dst):
        """
        Merge two lists using union by rank heuristic. Updates max_row_count with the new maximum
        table size.

        Args:
            src (list): Source list
            dst (list): Destination list

        """
        src_parent = self.find_parent(src)
        dst_parent = self.find_parent(dst)

        if src_parent == dst_parent:
            return

        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] += self.row_counts[dst_parent]
            self.row_counts[dst_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[src_parent])
        else:
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.row_counts[src_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[dst_parent])
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[dst_parent] += 1


def main():
    """
    Main method

    """
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    database = Database(counts)
    for _ in range(n_queries):
        dst, src = map(int, input().split())
        database.merge(dst - 1, src - 1)
        print(database.max_row_count)


if __name__ == "__main__":
    main()

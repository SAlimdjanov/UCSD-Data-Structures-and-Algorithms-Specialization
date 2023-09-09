"""
build_heap.py

"""


class MinimumBinaryHeap:
    """
    Creates a Minimum Binary Heap Object

    """

    def __init__(self, list_a):
        self.list_a = list_a
        self.heap_size = len(self.list_a)
        self.swaps_list = []

    def left_child(self, index):
        """
        Return the index of the left side child node given the index of the parent node.

        Args:
            index (int): Parent node index

        Returns:
            int: Index of the left child node

        """
        return 2 * index + 1

    def right_child(self, index):
        """
        Return the index of the right side child node given the index of the parent node.

        Args:
            index (int): Parent node index

        Returns:
            int: Index of the right child node

        """
        return 2 * index + 2

    def sift_down(self, index):
        """
        Sift an element in a binary tree down recursively.

        Args:
            index (int): Index of the element to sift down

        """
        min_index = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < self.heap_size and self.list_a[left] < self.list_a[min_index]:
            min_index = left

        if right < self.heap_size and self.list_a[right] < self.list_a[min_index]:
            min_index = right

        if min_index != index:
            self.swaps_list.append((index, min_index))
            self.list_a[index], self.list_a[min_index] = (
                self.list_a[min_index],
                self.list_a[index],
            )
            self.sift_down(min_index)

    def build_heap(self):
        """
        Build a heap from ``data`` inplace. Returns a sequence of swaps performed by the algorithm.

        """
        heap_size = self.heap_size
        for i in range(heap_size // 2 - 1, -1, -1):
            self.sift_down(i)


def main():
    """
    Main method

    """
    n = int(input())
    array = list(map(int, input().split()))
    assert len(array) == n

    min_bin_heap = MinimumBinaryHeap(array)
    MinimumBinaryHeap.build_heap(min_bin_heap)
    swaps = min_bin_heap.swaps_list
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

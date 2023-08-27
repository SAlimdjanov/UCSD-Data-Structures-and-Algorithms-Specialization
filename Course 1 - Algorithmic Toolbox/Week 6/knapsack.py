""" 
knapsack.py

"""


def maximum_gold(capacity, weights):
    """
    Maximizes the gold with a dictionary (hash table) and recursive memorization function

    Args:
        capacity (int): Bag capacity
        weights (int list): List of gold bar weights

    Returns:
        int: The maximum weight of gold that fits into the bag

    """
    len_weights, hash_dict = len(weights), {}

    def memorization(index, capacity_left):
        """
        Memorize the computation results in a hash table (dictionary). Recursively called

        Args:
            index (int): Index of weights list
            capacity_left (int): Remaining bag capacity

        Returns:
            int: Element of the hash table that contains the maximum weight

        """
        if index < 0:
            return 0

        # Check if the number has already been calculated
        if (index, capacity_left) in hash_dict:
            return hash_dict[(index, capacity_left)]

        # If the weight is greater than the capacity left, try the next weight element
        if weights[index] > capacity_left:
            hash_dict[(index, capacity_left)] = memorization(index - 1, capacity_left)

        else:
            included = (
                memorization(index - 1, capacity_left - weights[index]) + weights[index]
            )
            not_included = memorization(index - 1, capacity_left)
            hash_dict[(index, capacity_left)] = max(included, not_included)

        return hash_dict[(index, capacity_left)]

    return memorization(len_weights - 1, capacity)


if __name__ == "__main__":
    input_capacity, n = list(map(int, input().split()))
    input_weights = list(map(int, input().split()))
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))

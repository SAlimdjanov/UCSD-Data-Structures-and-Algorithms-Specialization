""" 
knapsack.py

"""


def maximum_gold(capacity, weights):
    """Maximizes the gold with a dictionary (hash table) and recursive memorization function"""
    len_weights, hash_dict = len(weights), {}

    def memorization(index, capacity_left):
        if index < 0:
            return 0
        if (index, capacity_left) in hash_dict:
            return hash_dict[(index, capacity_left)]
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

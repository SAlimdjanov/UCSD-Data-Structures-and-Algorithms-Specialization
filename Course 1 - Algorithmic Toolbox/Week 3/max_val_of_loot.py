""" 
max_val_of_loot.py

"""


def max_val_of_loot(bag_capacity, weight_list, cost_list):
    """
    Finds the maximum value of items that fit into the backpack

    Args:
        bag_capacity (int): Capacity of the backpack
        weight_list (int list): List of weights
        cost_list (int list): List of costs

    Returns:
        float: Maximum value of loot that fits into the backpack

    """
    if bag_capacity == 0 or not weight_list:
        return 0

    index, weight_len = -1, len(weight_list)
    max_cost_per_weight = 0

    for j in range(weight_len):
        if weight_list[j] > 0 and (cost_list[j] / weight_list[j]) > max_cost_per_weight:
            max_cost_per_weight = cost_list[j] / weight_list[j]
            index = j

    if index == -1:
        return 0

    amount = min(weight_list[index], bag_capacity)
    value = cost_list[index] * (amount / weight_list[index])
    weight_list[index] -= amount
    bag_capacity -= amount

    return value + max_val_of_loot(bag_capacity, weight_list, cost_list)


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    weights, costs = [0] * n, [0] * n

    for i in range(0, n):
        costs[i], weights[i] = map(int, input().split())

    print(max_val_of_loot(capacity, weights, costs))

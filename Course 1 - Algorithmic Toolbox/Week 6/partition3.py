""" 
partition3.py

"""


def sum_of_subset(values, num_n, num_a, num_b, num_c, ref_dict):
    """Sum of subsets"""
    if num_a == 0 and num_b == 0 and num_c == 0:
        return True
    if num_n < 0:
        return False
    key = f"{num_a}|{num_b}|{num_c}|{num_n}"
    if key not in ref_dict:
        flag_a, flag_b, flag_c = False, False, False
        if num_a - values[num_n] >= 0:
            flag_a = sum_of_subset(
                values, num_n - 1, num_a - values[num_n], num_b, num_c, ref_dict
            )
        if not flag_a and num_b - values[num_n] >= 0:
            flag_b = sum_of_subset(
                values, num_n - 1, num_a, num_b - values[num_n], num_c, ref_dict
            )
        if not flag_a and not flag_b and num_c - values[num_n] >= 0:
            flag_c = sum_of_subset(
                values, num_n - 1, num_a, num_b, num_c - values[num_n], ref_dict
            )
        ref_dict[key] = flag_a or flag_b or flag_c
    return ref_dict[key]


def partition3(values):
    """Splitting the pirate loot problem"""
    len_values = len(values)
    if len_values < 3:
        return 0
    ref_dict = {}
    total_sum = sum(values)
    if total_sum % 3 != 0:
        return 0
    target_sum = total_sum // 3
    if sum_of_subset(
        values, len_values - 1, target_sum, target_sum, target_sum, ref_dict
    ):
        return 1
    return 0


if __name__ == "__main__":
    input_n = int(input())
    input_values = list(map(int, input().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))

""" 
primitive_calculator.py

"""


def compute_operations(num_n):
    """Compute number of operations"""
    all_operations = [None] * (num_n + 1)
    all_min_operations = [0] + [None] * num_n
    for i in range(1, num_n + 1):
        current_operation = i - 1
        current_min_operations = all_min_operations[current_operation] + 1
        if i % 3 == 0:
            operation = i // 3
            num_operations = all_min_operations[operation] + 1
            if num_operations < current_min_operations:
                current_operation, current_min_operations = operation, num_operations
        if i % 2 == 0:
            operation = i // 2
            num_operations = all_min_operations[operation] + 1
            if num_operations < current_min_operations:
                current_operation, current_min_operations = operation, num_operations
        all_operations[i], all_min_operations[i] = (
            current_operation,
            current_min_operations,
        )
    numbers = []
    j = num_n
    while j > 0:
        numbers.append(j)
        j = all_operations[j]
    numbers.reverse()
    return numbers


if __name__ == "__main__":
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)

""" 
primitive_calculator.py

"""


def compute_operations(num_n):
    """
    Compute the minimum number of operations to get from num_n to 1

    Args:
        num_n (int): Input number

    Returns:
        int list: list which contains the sequence of intermediate numbers needed to get to n

    """
    # Create lists to store all operations and minimum operations
    all_operations = [None] * (num_n + 1)
    all_min_operations = [0] + [None] * num_n

    # Iterate from 1 to n + 1
    for i in range(1, num_n + 1):
        current_operation = i - 1
        current_min_operations = all_min_operations[current_operation] + 1

        # Check if the number can be divisible by 3. If so, change the operation
        if i % 3 == 0:
            operation = i // 3
            num_operations = all_min_operations[operation] + 1
            if num_operations < current_min_operations:
                current_operation, current_min_operations = operation, num_operations

        # Check if the number can be divisible by 2. If so, change the operation
        if i % 2 == 0:
            operation = i // 2
            num_operations = all_min_operations[operation] + 1
            if num_operations < current_min_operations:
                current_operation, current_min_operations = operation, num_operations

        # Update the all operations and min operations list
        all_operations[i], all_min_operations[i] = (
            current_operation,
            current_min_operations,
        )

    numbers = []
    j = num_n

    # Append all successful operations to the output list
    while j > 0:
        numbers.append(j)
        j = all_operations[j]

    # Reverse the numbers list as part of output requirements
    numbers.reverse()

    return numbers


if __name__ == "__main__":
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)

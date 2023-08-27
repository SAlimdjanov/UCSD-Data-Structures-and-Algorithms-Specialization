""" 
placing_parentheses.py

"""


def evaluate(num_a, num_b, operation):
    """
    Evaluate based on input operator

    Args:
        num_a (int): Integer A
        num_b (int): Integer B
        operation (str): Operator character

    Returns:
        int: Result of the operation on A and B

    """
    if operation == "+":
        return num_a + num_b
    if operation == "-":
        return num_a - num_b
    if operation == "*":
        return num_a * num_b
    assert False


def maximum_value(expression):
    """
    Solves the Placing parenthesis problem

    Args:
        expression (str): Expression string

    Returns:
        int: _Maximum possible result of the input expression

    """
    expression_len = len(expression)
    num_of_digits = (expression_len + 1) // 2

    # Create 2D lists to store results
    min_matrix = [[0] * num_of_digits for _ in range(num_of_digits)]
    max_matrix = [[0] * num_of_digits for _ in range(num_of_digits)]

    # Populate the lists with initial values
    for i in range(num_of_digits):
        min_matrix[i][i] = int(expression[2 * i])
        max_matrix[i][i] = int(expression[2 * i])

    # Iterate through the lists and populate both matrices with results
    for m in range(num_of_digits - 1):
        for i in range(num_of_digits - m - 1):
            j = i + m + 1
            min_matrix[i][j] = float("inf")
            max_matrix[i][j] = float("-inf")
            for k in range(i, j):
                operation = expression[2 * k + 1]
                num_a = evaluate(min_matrix[i][k], min_matrix[k + 1][j], operation)
                num_b = evaluate(min_matrix[i][k], max_matrix[k + 1][j], operation)
                num_c = evaluate(max_matrix[i][k], min_matrix[k + 1][j], operation)
                num_d = evaluate(max_matrix[i][k], max_matrix[k + 1][j], operation)
                min_matrix[i][j] = min(min_matrix[i][j], num_a, num_b, num_c, num_d)
                max_matrix[i][j] = max(max_matrix[i][j], num_a, num_b, num_c, num_d)

    # Return the maximum value of the maximum value matrix
    return max_matrix[0][num_of_digits - 1]


if __name__ == "__main__":
    input_expression = input()
    print(maximum_value(input_expression))

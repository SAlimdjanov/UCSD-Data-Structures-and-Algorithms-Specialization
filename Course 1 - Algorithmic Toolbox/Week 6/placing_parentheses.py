""" 
placing_parentheses.py

"""


def evaluate(num_a, num_b, operation):
    """Evaluate based on input operator"""
    if operation == "+":
        return num_a + num_b
    if operation == "-":
        return num_a - num_b
    if operation == "*":
        return num_a * num_b
    assert False


def maximum_value(expression):
    """Solves the Placing parenthesis problem"""
    expression_len = len(expression)
    num_of_digits = (expression_len + 1) // 2
    min_matrix = [[0] * num_of_digits for _ in range(num_of_digits)]
    max_matrix = [[0] * num_of_digits for _ in range(num_of_digits)]
    for i in range(num_of_digits):
        min_matrix[i][i] = int(expression[2 * i])
        max_matrix[i][i] = int(expression[2 * i])
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
    return max_matrix[0][num_of_digits - 1]


if __name__ == "__main__":
    input_expression = input()
    print(maximum_value(input_expression))

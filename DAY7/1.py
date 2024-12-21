from itertools import product

def evaluate_expression(nums, ops):
    """
    Evaluate equation with given numbers and operators from left to right.
    
    :param nums: List of numbers in the equation
    :param ops: List of operators ('+' or '*')
    :return: Calculated result
    """
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i+1]
        elif ops[i] == '*':
            result *= nums[i+1]
    return result

def find_valid_test_values(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        equations = file.readlines()

    for line in equations:
        test_value, nums = line.split(':')
        test_value = int(test_value.strip())
        nums = list(map(int, nums.split()))

        num_operators = len(nums) - 1
        possible_operators = product(['+', '*'], repeat=num_operators)

        valid_equation_found = False
        for operators in possible_operators:
            try:
                # Evaluate the expression with the current operators
                result = evaluate_expression(nums, operators)
                if result == test_value:
                    total_sum += test_value
                    valid_equation_found = True
                    break  # If one valid combination is found, move to next equation
            except Exception as e:
                # If there's an error evaluating this combination, skip it
                continue

        # Optional: Log if no valid combination was found for this test value
        if not valid_equation_found:
            print(f"No valid combination for {test_value}")

    return total_sum

# Example usage
file_path = 'C:\\code\\PYTHON\\2024Challanges\\DAY7\\data.txt'  # Ensure you have this file with the correct format
result = find_valid_test_values(file_path)
print("Total Calibration Result:", result)

# eval() 会按照 Python 默认的运算规则解析表达式，即运算符的优先级、括号等
def concatenate(a, b):
    """
    Concatenate two numbers
    
    :param a: First number
    :param b: Second number
    :return: Concatenated number
    """
    return int(str(a) + str(b))

def evaluate_equation(nums, ops):
    """
    Evaluate equation with given numbers and operators from left to right
    
    :param nums: List of numbers in the equation
    :param ops: List of operators ('+', '*', or '||')
    :return: Calculated result
    """
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i+1]
        elif ops[i] == '*':
            result *= nums[i+1]
        else:  # concatenation
            result = concatenate(result, nums[i+1])
    return result

def solve_equations(equations):
    """
    Solve equations by trying all possible operator combinations
    
    :param equations: Dictionary of test values and their number lists
    :return: List of test values that can be produced
    """
    valid_equations = []
    
    for test_val, nums in equations.items():
        # Number of positions to insert operators is len(nums) - 1
        valid_ways = 0
        
        # Generate all possible operator combinations (+, *, ||)
        from itertools import product
        for ops_combo in product(['+', '*', '||'], repeat=len(nums)-1):
            try:
                # Evaluate equation with this operator combination
                if evaluate_equation(nums, ops_combo) == test_val:
                    valid_ways += 1
            except Exception:
                # Skip invalid combinations
                continue
        
        # If at least one valid combination exists, add to results
        if valid_ways > 0:
            valid_equations.append(test_val)
    
    return valid_equations

def parse_input(input_text):
    """
    Parse input text into a dictionary of test values and number lists
    
    :param input_text: Raw input text
    :return: Dictionary of equations
    """
    equations = {}
    for line in input_text.strip().split('\n'):
        test_val, nums_str = line.split(': ')
        nums = [int(x) for x in nums_str.split()]
        equations[int(test_val)] = nums
    
    return equations

def main(input_file):
    """
    Main solver function, reads input from a file.
    
    :param input_file: File path for the input data
    :return: Total calibration result
    """
    with open(input_file, 'r') as file:
        input_text = file.read()
    
    equations = parse_input(input_text)
    valid_equations = solve_equations(equations)
    return sum(valid_equations)

# Example usage
input_file = '2024Challanges/DAY7/data.txt'  # Replace with the actual file path
print("Example Test Result (Part Two):", main(input_file))

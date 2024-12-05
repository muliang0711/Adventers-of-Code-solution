import re

def process_multiplications(filename):
    # Step 1: Read the corrupted memory data from the file
    with open(filename, 'r') as file:
        data = file.read()

    # Step 2: Define the regex pattern to match mul(x, y) with integers of 1 to 3 digits
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"  # This will match mul(x, y) where x and y are integers with 1 to 3 digits

    # Step 3: Initialize a flag to track whether mul() operations are enabled or not
    process_mul = True  # Initially, mul() operations are enabled by default
    results = []

    # Step 4: Iterate through the data and handle do() and don't() instructions
    instructions = data.split()  # Split data into individual instructions or tokens

    for instruction in instructions:
        if instruction == "do()":
            # Enable future mul() operations
            process_mul = True
        elif instruction == "don't()":
            # Disable future mul() operations
            process_mul = False
        elif "mul(" in instruction:  # This is a multiplication expression
            # Extract the numbers from the mul(x, y) pattern
            match = re.search(pattern, instruction)
            if match and process_mul:
                # If process_mul is True, perform the multiplication
                num1, num2 = map(int, match.groups())
                result = num1 * num2
                results.append(result)

    # Step 5: Calculate the sum of all results
    total_sum = sum(results)

    # Step 6: Return the sum of the results
    return total_sum

# Example usage
filename = r"C:\code\PYTHON\challanges\DAY3\data.txt"  # Replace with the correct path to your file
total_sum = process_multiplications(filename)
print(f"Total sum of valid mul() operations: {total_sum}")

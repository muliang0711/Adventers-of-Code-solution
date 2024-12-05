import re

def process_multiplications(filename):
    # Step 1: Read the corrupted memory data from the file
    with open(filename, 'r') as file:
        data = file.read()

    # Step 2: Define the regex pattern to match mul(x, y) with integers of 1 to 3 digits
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"  # This will match mul(x, y) where x and y are integers with 1 to 3 digits

    # Step 3: Use re.findall() to find all matches of the pattern
    matches = re.findall(pattern, data)

    # Step 4: Initialize a list to store the results of the multiplications
    results = []

    # Step 5: Loop through the matches and perform the multiplications
    for match in matches:
        # Extract the two numbers from the match
        num1, num2 = map(int, match)  # Convert both to integers
        # Perform the multiplication
        result = num1 * num2
        # Add the result to the results list
        results.append(result)

    # Step 6: Return the list of results
    return results

# Example usage
filename = r"C:\code\PYTHON\challanges\DAY3\data.txt"  # Replace with the correct path
results = process_multiplications(filename)
total_result = sum(results)

print(total_result)

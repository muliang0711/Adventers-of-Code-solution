import re

def process_with_toggling(data):
    # Define the patterns for mul(), do(), and don't()
    pattern_mul = r"mul\((\d{1,3}),(\d{1,3})\)"  # To match mul(x, y)
    pattern_do = r"do\(\)"  # To match 'do()'
    pattern_dont = r"don't\(\)"  # To match 'don't()'

    # Initialize the flag to True (active)
    active = True

    # Use re.findall() to find all matches for mul(), do(), and don't()
    matches = re.findall(f"({pattern_mul}|{pattern_do}|{pattern_dont})", data)
    #print(matches)
    # Initialize a list to store the results of the multiplications
    results = []

    # Loop through the matches and perform actions based on the patterns
    for match in matches:
        print(match)
        if match[0].startswith("mul"):
            if active:
                # Extract the two numbers from the match
                num1, num2 = map(int, match[0].strip("mul()").split(","))
                # Perform the multiplication
                result = num1 * num2
                # Add the result to the results list
                results.append(result)
        elif match[0] == "do()":
            active = True  # Turn the function back on (active)
        elif match[0] == "don't()":
            active = False  # Turn the function off (inactive)

    # Return the list of results
    return results


# Load data from the file
with open('C:\\code\\PYTHON\\2024Challanges\\DAY3\\data.txt', 'r') as file:
    data = file.read()

# Process the data directly with toggling behavior
multiplication_results = process_with_toggling(data)

# Calculate the total sum of the multiplication results
total = sum(multiplication_results)

# Print the multiplication results and the total sum
print("Multiplication Results with Toggling:", multiplication_results)
print("Total Sum:", total)

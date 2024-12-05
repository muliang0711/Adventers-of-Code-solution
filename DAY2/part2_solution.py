def is_increase(levels):
    """Check if the levels are strictly increasing and the difference between adjacent levels is between 1 and 3."""
    for i in range(len(levels) - 1):
        diff = levels[i+1] - levels[i]
        # Check if the difference is between 1 and 3 and if the sequence is increasing
        if diff < 1 or diff > 3 or levels[i] >= levels[i + 1]:
            return False
    return True

def is_decrease(levels):
    """Check if the levels are strictly decreasing and the difference between adjacent levels is between 1 and 3."""
    for i in range(len(levels) - 1):
        diff = levels[i] - levels[i+1]
        # Check if the difference is between 1 and 3 and if the sequence is decreasing
        if diff < 1 or diff > 3 or levels[i] <= levels[i + 1]:
            return False
    return True

def check_with_one_removal(levels):
    """Check if removing one level from the report can make it safe (either strictly increasing or decreasing)."""
    # Try removing each level one by one and check if the remaining levels form a safe report
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]  # Remove the level at index i
        if is_increase(new_levels) or is_decrease(new_levels):
            return True  # If removing one level makes it safe, return True
    return False  # If no removal makes it safe, return False

def check_reports(filename):
    safe_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            # Convert the line into a list of integers (levels)
            levels = list(map(int, line.strip().split()))
            
            # Check if the report is already safe (either strictly increasing or strictly decreasing)
            if is_increase(levels) or is_decrease(levels):
                safe_count += 1
            # If not safe, check if it can become safe by removing one level
            elif check_with_one_removal(levels):
                safe_count += 1
                
    return safe_count

# Example usage
filename = "C:\\code\\PYTHON\\challanges\\DAY2\\data.txt"  # Adjust the file path as needed
safe_count = check_reports(filename)
print(f"Number of safe reports: {safe_count}")

# SUCESS 
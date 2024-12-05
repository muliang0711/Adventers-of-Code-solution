def total_distance_from_file(filename):
    left_list = []
    right_list = []
    
    # Read the file and parse the numbers
    with open(filename, 'r') as file:
        for line in file:
            # Split each line into two numbers and add to the respective lists
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Initialize the total distance
    total_dist = 0
    
    # Calculate the sum of absolute differences between corresponding elements
    for left, right in zip(left_list, right_list):
        total_dist += abs(left - right)
    
    return total_dist

# Example usage:
filename = 'C:\code\PYTHON\challanges\DAY1\data.txt'  # Change this to the path of your file
result = total_distance_from_file(filename)
print("Total distance:", result)

# SUCESS 
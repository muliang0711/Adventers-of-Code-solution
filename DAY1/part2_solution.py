def extract_and_process_xy_from_file(filename):
    x_list = []
    y_list = []
    
    # Read the file and extract the numbers as x and y
    with open(filename, 'r') as file:
        for line in file:
            # Split each line into two numbers, assign them as x and y
            x, y = map(int, line.split())
            x_list.append(x)
            y_list.append(y)
    
    # Process each x and y pair using a for loop
    for x, y in zip(x_list, y_list):
        # Your code for processing x and y goes here
        # For now, we just print x and y as you asked
        print(f"x: {x}, y: {y}")
   # Initialize a set to track unique numbers in x
    seen = set()
    
    # Iterate through x_list and detect unique numbers
    for x in x_list:
        if x not in seen:
            seen.add(x)
            # Count how many times x appears in y_list
            count_in_y = y_list.count(x)
            print(f"Unique number in x: {x}, appears {count_in_y} times in y.")

# Example usage:
filename = 'C:\code\PYTHON\challanges\DAY1\data.txt'  # Change this to the path of your file
extract_and_process_xy_from_file(filename)


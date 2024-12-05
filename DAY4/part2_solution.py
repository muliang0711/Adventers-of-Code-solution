def count_xmas_x_from_file(file_path):
    # Step 1: Read the grid data from the file
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    rows = len(grid)
    cols = len(grid[0])
    target = "MAS"
    count = 0

    # Step 2: Iterate over all possible center cells for the "X"
    for i in range(1, rows - 1):  # Ensuring we don't go out of bounds
        for j in range(1, cols - 1):
            # Step 3: Check the four diagonal directions forming the X
            #-- 1. Top-left to center to bottom-right (forwards)
            if grid[i-1][j-1] == 'M' and grid[i][j] == 'A' and grid[i+1][j+1] == 'S':
                count += 1

            # 4. Bottom-left to center to top-right (backwards)
            if grid[i+1][j-1] == 'M' and grid[i][j] == 'A' and grid[i-1][j+1] == 'S':
                count += 1

    return count

# Usage example:
file_path = 'C:\code\PYTHON\challanges\DAY4\data.txt'  # Replace with the actual file path
result = count_xmas_x_from_file(file_path)
print(f"Total X-MAS X occurrences: {result}")

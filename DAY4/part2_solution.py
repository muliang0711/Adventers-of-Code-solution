def read_grid(file_path):
    """Reads the grid from the file."""
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]
    
    return grid


def count_crosses(grid):
    """Count 'crosses' based on the 'A' surrounded by 'M' and 'S'."""
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for row in range(1, rows - 1):  # Avoid edges
        for col in range(1, cols - 1):  # Avoid edges
            if grid[row][col] == 'A':
                # Check the four diagonals for the required pattern
                up_left = grid[row-1][col-1]
                up_right = grid[row-1][col+1]
                down_left = grid[row+1][col-1]
                down_right = grid[row+1][col+1]
                
                # Check if the diagonals match the pattern for a valid cross
                backslash = (up_left == 'M' and down_right == 'S') or (up_left == 'S' and down_right == 'M')
                forwslash = (up_right == 'M' and down_left == 'S') or (up_right == 'S' and down_left == 'M')
                
                if backslash and forwslash:
                    count += 1
    
    return count


# Example usage
file_path = 'C://code//PYTHON//2024Challanges//DAY4//data.txt'  # Path to your file
grid = read_grid(file_path)

# Call the improved function to count crosses
crosses_count = count_crosses(grid)

# Print the total occurrences of the pattern
print(f"'XMAS' found {crosses_count} times.")  # Output the result

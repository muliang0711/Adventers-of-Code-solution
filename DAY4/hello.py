def read_grid(file_path):
    """Reads the grid from the file."""
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Print out the size of the grid

    
    # Display the grid (2D array of characters)


    return grid


count = 0  # Global count to track number of "XMAS" found

def horizontal(grid):
    """Search for "XMAS" horizontally (left to right)."""
    global count
    rows = len(grid)
    
    for i in range(rows):
        for j in range(len(grid[i]) - 3):  # We need at least 4 characters to match "XMAS"
            if grid[i][j:j+4] == "XMAS":
                count += 1  # Increment count when "XMAS" is found
    return count  # Return the total count of "XMAS" found horizontally

def horizontal_return(grid):
    """Search for "XMAS" backwards horizontally (right to left)."""
    global count
    rows = len(grid)
    
    for i in range(rows):
        for j in range(len(grid[i]) - 3):
            if grid[i][j:j+4] == "SMAX":
                count += 1
    return count

def vertical(grid):
    """Search for "XMAS" vertically (top to bottom)."""
    global count
    rows = len(grid)
    cols = len(grid[0])
    
    for j in range(cols):  # Iterate through each column
        for i in range(rows - 3):  # We need at least 4 characters vertically
            if (grid[i][j] == 'X' and grid[i+1][j] == 'M' and grid[i+2][j] == 'A' and grid[i+3][j] == 'S'):
                count += 1  # Increment count when "XMAS" is found vertically
    return count

def vertical_return(grid):
    """Search for "XMAS" backwards vertically (bottom to top)."""
    global count
    rows = len(grid)
    cols = len(grid[0])
    
    for j in range(cols):  # Iterate through each column
        for i in range(rows - 3):  # We need at least 4 characters vertically
            if (grid[i][j] == 'S' and grid[i+1][j] == 'A' and grid[i+2][j] == 'M' and grid[i+3][j] == 'X'):
                count += 1  # Increment count when "XMAS" is found vertically (backwards)
    return count

def diagonal(grid):
    """Search for "XMAS" diagonally from top-left to bottom-right."""
    global count
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows - 3):  # Ensure we don't go out of bounds
        for j in range(cols - 3):  # Ensure we don't go out of bounds
            if (grid[i][j] == 'X' and grid[i+1][j+1] == 'M' and grid[i+2][j+2] == 'A' and grid[i+3][j+3] == 'S'):
                count += 1  # Increment count when "XMAS" is found diagonally (top-left to bottom-right)
    return count

def diagonal_return(grid):
    """Search for "XMAS" backwards diagonally from bottom-right to top-left."""
    global count
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows - 3):  # Ensure we don't go out of bounds
        for j in range(cols - 3):  # Ensure we don't go out of bounds
            if (grid[i][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'M' and grid[i+3][j+3] == 'X'):
                count += 1  # Increment count when "XMAS" is found diagonally (top-left to bottom-right)
    return count

def diagonal_toright(grid):
    """Search for "XMAS" diagonally from bottom-left to top-right."""
    global count
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows - 3):  # Ensure we don't go out of bounds
        for j in range(3, cols):  # Ensure we don't go out of bounds
            if (grid[i][j] == 'X' and grid[i+1][j-1] == 'M' and grid[i+2][j-2] == 'A' and grid[i+3][j-3] == 'S'):
                count += 1  # Increment count when "XMAS" is found diagonally (bottom-left to top-right)
    return count

def diagonal_toright_return(grid):
    """Search for "XMAS" backwards diagonally from top-right to bottom-left."""
    global count
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows - 3):  # Ensure we don't go out of bounds
        for j in range(3, cols):  # Ensure we don't go out of bounds
            if (grid[i][j] == 'S' and grid[i+1][j-1] == 'A' and grid[i+2][j-2] == 'M' and grid[i+3][j-3] == 'X'):
                count += 1  # Increment count when "XMAS" is found diagonally (top-right to bottom-left)
    return count

# Example usage
file_path = 'C:/code/PYTHON/challanges/DAY4/data.txt'   # Path to your file
grid = read_grid(file_path)



# Perform the searches for all directions
horizontal(grid)
horizontal_return(grid)
vertical(grid)
vertical_return(grid)
diagonal(grid)
diagonal_return(grid)
diagonal_toright(grid)
diagonal_toright_return(grid)

# Print the total occurrences of 'XMAS' after all the searches
print(f"'XMAS' found {count} times.") # 2357

def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_length = len(word)
    directions = [
        (0, 1),  # right (horizontal)
        (0, -1), # left (horizontal)
        (1, 0),  # down (vertical)
        (-1, 0), # up (vertical)
        (1, 1),  # down-right (diagonal)
        (1, -1), # down-left (diagonal)
        (-1, 1), # up-right (diagonal)
        (-1, -1) # up-left (diagonal)
    ]
    
    # Function to check if word "XMAS" starts from (r, c) in a given direction (dr, dc)
    def check_word(r, c, dr, dc):
        for i in range(word_length):
            nr, nc = r + dr * i, c + dc * i
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True
    
    count = 0  # Initialize the counter for successful finds
    
    # Traverse the grid and check all directions for the word "XMAS"
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':  # Only start looking for "XMAS" if the character is 'X'
                for dr, dc in directions:
                    if check_word(r, c, dr, dc):
                        count += 1  # Increment the counter each time we find "XMAS"
    
    return count

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        # Read each line from the file and strip any trailing newlines or spaces
        grid = [line.strip() for line in file.readlines()]
    return grid

# Example usage
filename = 'C:\\code\\PYTHON\\2024Challanges\\DAY4\\data.txt'  # File containing the grid
grid = read_grid_from_file(filename)
result = find_xmas(grid)
print(f"Total occurrences of XMAS: {result}") #2545

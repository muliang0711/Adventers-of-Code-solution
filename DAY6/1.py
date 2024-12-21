def navigate_grid(grid, start_x, start_y, start_direction):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    visited = set([(start_x, start_y)])
    current_x, current_y = start_x, start_y
    current_direction = start_direction
    
    while True:
        # Try to move in the current direction
        dx, dy = directions[current_direction]
        new_x, new_y = current_x + dx, current_y + dy
        
        # Check if the move is valid
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '.':
            current_x, current_y = new_x, new_y
            visited.add((current_x, current_y))
            print(f"Moving to ({current_x}, {current_y}) in direction {current_direction}")
        else:
            # Turn right if can't move forward
            current_direction = turn_right[current_direction]
            print(f"Cannot move in direction {current_direction}, turning right")
            
            # Try to move in the new direction
            dx, dy = directions[current_direction]
            new_x, new_y = current_x + dx, current_y + dy
            
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '.':
                current_x, current_y = new_x, new_y
                visited.add((current_x, current_y))
                print(f"Moving to ({current_x}, {current_y}) after turning in direction {current_direction}")
            else:
                # If can't move in new direction, we're stuck
                break
        
        # Optional: stop if we've reached a boundary
        if (current_x == 0 or current_x == len(grid) - 1 or 
            current_y == 0 or current_y == len(grid[0]) - 1):
            break
    
    return visited

# Read the grid from the file
with open('C:\\code\\PYTHON\\2024Challanges\\DAY6\\data.txt', 'r') as file:
    grid = []
    for line in file:
        grid.append(list(line.strip()))

# Find the starting position of the direction symbols
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] in ['^', 'v', '>', '<']:
            start_position = (x, y)
            direction = grid[x][y]
            grid[x][y] = '.'  # Mark start position as empty
            
            print(f"Starting at position {start_position} with direction {direction}")
            visited = navigate_grid(grid, x, y, direction)
            print("Visited positions:", len(visited))
            break
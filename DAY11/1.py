def transform_stone(stone):
    stone_str = str(stone)
    
    # Rule 1: If stone is 0, replace with 1
    if stone == 0:
        return [1]
    
    # Rule 2: If even number of digits, split in half
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        return [left, right]
    
    # Rule 3: Multiply by 2024
    return [stone * 2024]

def simulate_blink(stones):
    new_stones = []
    for stone in stones:
        new_stones.extend(transform_stone(stone))
    return new_stones

def count_stones_after_blinks(initial_stones, blinks):
    stones = initial_stones.copy()
    for _ in range(blinks):
        stones = simulate_blink(stones)
    return len(stones)

# Function to run the puzzle
def solve_puzzle(input_stones):
    return count_stones_after_blinks(input_stones, 75)

# Correct input example
input_stones = [475449 ,2599064 ,213 ,0, 2 ,65, 5755, 51149]
result = solve_puzzle(input_stones)
print(f"Number of stones after 75 blinks: {result}")

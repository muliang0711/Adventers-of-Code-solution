def parse_disk_map_from_file(filename):
    """Read and parse disk map from file."""
    with open(filename, 'r') as f:
        disk_map = f.read().strip()
    return [int(x) for x in disk_map]

def create_block_representation(lengths):
    """Convert lengths into efficient block representation using generators."""
    file_id = 0
    for i in range(0, len(lengths), 2):
        # Add file blocks
        file_len = lengths[i]
        for _ in range(file_len):
            yield file_id
        file_id += 1
        
        # Add free space if not at the end
        if i + 1 < len(lengths):
            space_len = lengths[i + 1]
            for _ in range(space_len):
                yield '.'

def find_moves(blocks):
    """Find all required moves efficiently."""
    moves = []
    right_pos = len(blocks) - 1
    
    # Find all required moves in one pass
    while right_pos > 0:
        # Find rightmost file
        while right_pos >= 0 and blocks[right_pos] == '.':
            right_pos -= 1
        if right_pos < 0:
            break
            
        # Find leftmost space before this file
        left_pos = 0
        while left_pos < right_pos and blocks[left_pos] != '.':
            left_pos += 1
            
        if left_pos >= right_pos:
            break
            
        moves.append((right_pos, left_pos, blocks[right_pos]))
        # Update blocks for next iteration
        blocks[left_pos] = blocks[right_pos]
        blocks[right_pos] = '.'
        
    return moves, blocks

def calculate_checksum(blocks):
    """Calculate checksum efficiently using generator."""
    return sum(pos * int(block) for pos, block in enumerate(blocks) 
              if block != '.')

def process_large_disk(filename):
    """Process large disk data efficiently."""
    # Read lengths from file
    lengths = parse_disk_map_from_file(filename)
    
    # Create initial block representation
    blocks = list(create_block_representation(lengths))
    
    # Find all required moves
    moves, final_blocks = find_moves(blocks)
    
    # Calculate final checksum
    checksum = calculate_checksum(final_blocks)
    
    return {
        'total_moves': len(moves),
        'checksum': checksum,
        'final_length': len(final_blocks)
    }

def save_moves_to_file(moves, output_filename):
    """Save moves to file for later reference."""
    with open(output_filename, 'w') as f:
        for right_pos, left_pos, file_id in moves:
            f.write(f"Move file {file_id} from position {right_pos} to {left_pos}\n")

# Example usage
def main():
    try:
        result = process_large_disk('2024Challanges/DAY8/data.txt')
        print(f"Processed disk compaction:")
        print(f"Total moves required: {result['total_moves']}")
        print(f"Final checksum: {result['checksum']}")
        print(f"Final disk length: {result['final_length']}")
    except Exception as e:
        print(f"Error processing disk: {e}")

if __name__ == "__main__":
    main()
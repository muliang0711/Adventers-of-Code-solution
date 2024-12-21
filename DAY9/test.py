def parse_disk_map(disk_map):
    # Parse alternating file and space lengths into blocks
    lengths = [int(x) for x in list(disk_map)]
    blocks = []
    file_id = 0
    
    # Convert lengths into actual block representation
    pos = 0
    for i in range(0, len(lengths), 2):
        file_len = lengths[i]
        # Add file blocks
        for _ in range(file_len):
            blocks.append(file_id)
        file_id += 1
        
        # Add free space if not at the end
        if i + 1 < len(lengths):
            space_len = lengths[i + 1]
            for _ in range(space_len):
                blocks.append('.')
    
    return blocks

def visualize_blocks(blocks):
    return ''.join(str(x) for x in blocks)

def compact_disk(blocks):
    steps = [blocks.copy()]
    # when condition is false than can start the resoft process 
    while True:
        # Find rightmost file block
        right_file_pos = len(blocks) - 1
        while right_file_pos >= 0 and blocks[right_file_pos] == '.':
            right_file_pos -= 1
            
        if right_file_pos < 0:
            break
            
        # Find leftmost free space
        left_space_pos = 0
        while left_space_pos < right_file_pos and blocks[left_space_pos] != '.':
            left_space_pos += 1
            
        if left_space_pos >= right_file_pos:
            break
            
        # Move the block
        blocks[left_space_pos] = blocks[right_file_pos]
        blocks[right_file_pos] = '.'
        steps.append(blocks.copy())
    
    return steps

def calculate_checksum(blocks):
    checksum = 0
    for pos, block in enumerate(blocks):
        if block != '.':
            checksum += pos * int(block)
    return checksum

def solve_disk_compaction(disk_map):
    # Parse initial state
    blocks = parse_disk_map(disk_map)
    # print("Initial state:")
    # print(visualize_blocks(blocks))
    
    # Perform compaction
    steps = compact_disk(blocks)
    # print("\nCompaction steps:")
    # for step in steps:
    #    print(visualize_blocks(step))
    
    # Calculate checksum
    checksum = calculate_checksum(steps[-1])
    print(f"\nFinal checksum: {checksum}")
    return checksum

# Test with example input
example = "2333133121414131402"
result = solve_disk_compaction(example)

# the diffcult part is how to resoft 
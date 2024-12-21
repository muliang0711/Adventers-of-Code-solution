def parse_input(input_text):
    # Split input into sections
    rules_section, updates_section = input_text.strip().split('\n\n')
    
    # Parse ordering rules
    rules = {}
    for rule in rules_section.split('\n'):
        before, after = map(int, rule.split('|'))
        if before not in rules:
            rules[before] = set()
        rules[before].add(after)
    
    # Parse updates
    updates = [list(map(int, update.split(','))) for update in updates_section.split('\n')]
    
    return rules, updates

def is_update_ordered(update, rules):
    # Check if the update follows all applicable ordering rules
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if (update[i] in rules and update[j] in rules[update[i]]):
                return False
    return True

def solve_part_one(input_text):
    rules, updates = parse_input(input_text)
    
    # Find correctly ordered updates and their middle pages
    middle_pages = []
    for update in updates:
        if is_update_ordered(update, rules):
            middle_pages.append(update[len(update)//2])
    
    return sum(middle_pages)

def correct_update_order(update, rules):
    # Create a graph of dependencies
    graph = {page: set() for page in update}
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if (update[i] in rules and update[j] in rules[update[i]]):
                graph[update[j]].add(update[i])
    
    # Topological sort
    def dfs(node, visited, stack):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(node)
    
    visited = set()
    stack = []
    for node in update:
        if node not in visited:
            dfs(node, visited, stack)
    
    return stack[::-1]

def solve_part_two(input_text):
    rules, updates = parse_input(input_text)
    
    # Find and correct incorrectly ordered updates
    middle_pages = []
    for update in updates:
        if not is_update_ordered(update, rules):
            corrected = correct_update_order(update, rules)
            middle_pages.append(corrected[len(corrected)//2])
    
    return sum(middle_pages)

# Read input from file
with open('C:\\code\\PYTHON\\2024Challanges\\DAY5\\data.txt', 'r') as file:
    input_text = file.read()

# Solve both parts
print("Part One:", solve_part_one(input_text))
print("Part Two:", solve_part_two(input_text))
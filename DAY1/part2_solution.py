# File path for the input data
file_path = "C:\\code\\PYTHON\\2024Challanges\\DAY1\\data.txt"

# Initialize the lists
left_list = []
right_list = []

# Read data from the file
with open(file_path, 'r') as file:
    for line in file:
        # Split each line into two numbers
        a, b = map(int, line.split())
        left_list.append(a)
        right_list.append(b)

# Count the occurrences of each number in the right list
right_count = {}
for num in right_list:
    if num in right_count:
        right_count[num] += 1
    else:
        right_count[num] = 1

# Initialize similarity score
similarity_score = 0

# Calculate the similarity score by checking the occurrence in the right list
for num in left_list:
    similarity_score += num * right_count.get(num, 0)

# Output the final similarity score
print("Similarity Score:", similarity_score)
print(left_list)
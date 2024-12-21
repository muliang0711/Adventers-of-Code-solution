def parse_garden(input_text: str) -> list[str]:
    """Convert the input text into a list of strings, one for each row."""
    return [line.strip() for line in input_text.strip().split('\n')]

def find_regions(garden: list[str]) -> list[set[tuple[int, int]]]:
    """Find all connected regions of same-type plants."""
    height, width = len(garden), len(garden[0])
    visited = set()
    regions = []

    def get_neighbors(x: int, y: int) -> list[tuple[int, int]]:
        """Get valid neighboring coordinates."""
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < height and 0 <= new_y < width:
                neighbors.append((new_x, new_y))
        return neighbors

    def find_connected_region(x: int, y: int, plant_type: str) -> set[tuple[int, int]]:
        """Find all connected plots of the same plant type using DFS."""
        region = set()
        stack = [(x, y)]
        while stack:
            curr_x, curr_y = stack.pop()
            if (curr_x, curr_y) in region:
                continue
            region.add((curr_x, curr_y))
            visited.add((curr_x, curr_y))
            for next_x, next_y in get_neighbors(curr_x, curr_y):
                if garden[next_x][next_y] == plant_type and (next_x, next_y) not in visited:
                    stack.append((next_x, next_y))
        return region

    for i in range(height):
        for j in range(width):
            if (i, j) not in visited:
                region = find_connected_region(i, j, garden[i][j])
                regions.append(region)

    return regions

def calculate_perimeter(region: set[tuple[int, int]], garden: list[str]) -> int:
    """Calculate the perimeter of a region."""
    perimeter = 0
    plant_type = garden[list(region)[0][0]][list(region)[0][1]]
    for x, y in region:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if (new_x < 0 or new_x >= len(garden) or new_y < 0 or new_y >= len(garden[0]) or 
                garden[new_x][new_y] != plant_type):
                perimeter += 1
    return perimeter

def calculate_total_price(garden: list[str]) -> int:
    """Calculate the total price for fencing all regions."""
    regions = find_regions(garden)
    total_price = 0
    region_details = []
    for region in regions:
        area = len(region)
        perimeter = calculate_perimeter(region, garden)
        price = area * perimeter
        plant_type = garden[list(region)[0][0]][list(region)[0][1]]
        total_price += price
        region_details.append((plant_type, area, perimeter, price))
    print("\nRegion details:")
    for plant_type, area, perimeter, price in sorted(region_details):
        print(f"Plant {plant_type}: Area={area}, Perimeter={perimeter}, Price={price}")
    return total_price

if __name__ == "__main__":
    with open("2024Challanges/DAY12/data.txt", "r") as file:
        garden_input = file.read()

    garden = parse_garden(garden_input)
    print(f"\nGarden dimensions: {len(garden)} rows x {len(garden[0])} columns")
    result = calculate_total_price(garden)
    print(f"\nTotal fencing price: {result}")

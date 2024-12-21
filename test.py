# 定义一个函数来检查当前位置是否有效
def is_valid_move(x, y, maze, visited):
    # 确保x, y在迷宫范围内，并且该位置是空白区域且没有被访问过
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0 and (x, y) not in visited

# 定义DFS算法
def dfs(maze, x, y, visited, path):
    # 如果到达迷宫的边界（假设边界为出口）
    if x == len(maze) - 1 or y == len(maze[0]) - 1:  # 到达边界
        path.append((x, y))  # 将当前点加入路径
        return True
    
    # 如果当前位置有效且没有被访问过
    if is_valid_move(x, y, maze, visited):
        visited.add((x, y))  # 标记当前位置已访问
        path.append((x, y))  # 将当前位置加入路径
        
        # 尝试四个方向：上、下、左、右
        if (dfs(maze, x + 1, y, visited, path) or  # 向下
            dfs(maze, x - 1, y, visited, path) or  # 向上
            dfs(maze, x, y + 1, visited, path) or  # 向右
            dfs(maze, x, y - 1, visited, path)):   # 向左
            return True
        
        # 如果所有方向都走不通，回溯，移除当前路径
        path.pop()
    
    return False

# 主函数
def solve_maze(maze):
    visited = set()  # 记录已访问的位置
    path = []        # 用来存储从起点到出口的路径
    if dfs(maze, 0, 0, visited, path):  # 从起点(0, 0)开始
        return path
    else:
        return "No path found"

# 测试
maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

path = solve_maze(maze)
print(path)

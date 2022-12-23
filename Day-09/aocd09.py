from typing import List
from collections import deque
import sys

def parse(file_input: str) -> List[List[int]]:
    result = file_input.strip().split("\n")
    for i in range(len(result)):
        result[i] = list(map(int, list(result[i])))
    return result


def is_low_point(grid: List[List[int]], row: int, col: int, num_rows: int, num_cols: int) -> bool:
    # Check the 4 corners
    if row == 0 and col == 0:
        return grid[row][col] < grid[row+1][col] and grid[row][col] < grid[row][col+1]

    elif row == 0 and col == num_cols-1:
        return grid[row][col] < grid[row+1][col] and grid[row][col] < grid[row][col-1]

    elif row == num_rows-1 and col == 0:
        return grid[row][col] < grid[row-1][col] and grid[row][col] < grid[row][col+1]

    elif row == num_rows-1 and col == num_cols-1:
        return grid[row][col] < grid[row-1][col] and grid[row][col] < grid[row][col-1]

    # Check each of the four sides
    elif row == 0:
        return grid[row][col] < grid[row+1][col] and grid[row][col] < grid[row][col-1]\
    and grid[row][col] < grid[row][col+1]

    elif col == 0:
        return grid[row][col] < grid[row-1][col] and grid[row][col] < grid[row+1][col]\
    and grid[row][col] < grid[row][col+1]

    elif row == num_rows-1:
        return grid[row][col] < grid[row-1][col] and grid[row][col] < grid[row][col-1]\
    and grid[row][col] < grid[row][col+1]

    elif col == num_cols-1:
        return grid[row][col] < grid[row-1][col] and grid[row][col] < grid[row+1][col]\
    and grid[row][col] < grid[row][col-1]

    else:
        return grid[row][col] < grid[row-1][col] and grid[row][col] < grid[row+1][col]\
    and grid[row][col] < grid[row][col-1] and grid[row][col] < grid[row][col+1]


def partOne(grid: List[List[int]]) -> int:
    risk_level = 0
    low_points = []
    num_rows = len(grid)
    num_cols = len(grid[0])
    for row in range(num_rows):
        for col in range(num_cols):
            if is_low_point(grid, row, col, num_rows, num_cols):
                risk_level += grid[row][col] + 1
                low_points.append([row, col])

    return risk_level, low_points


def partTwo(grid: List[List[int]], low_points: List[List[int]]) -> int:
    visited = set()
    num_rows = len(grid)
    num_cols = len(grid[0])

    def bfs(row: int, col: int) -> int:
        size = 0
        q = deque()
        visited.add((row, col))
        q.append((row, col))
        size += 1
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                if (r + dr in range(num_rows)) and (c + dc in range(num_cols)) \
                and grid[r][c] < grid[r+dr][c+dc] and grid[r+dr][c+dc] != 9 \
                and (r+dr, c+dc) not in visited:
                    visited.add((r+dr, c+dc))
                    q.append((r+dr, c+dc))
                    size += 1
        return size

    result = 1
    sizes = []

    for row, col in low_points:
        if (row, col) not in visited:
            sizes.append(bfs(row, col))

    sizes.sort(reverse=True)

    for i in range(3):
        result *= sizes[i]

    return result

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        file_input = f.read()
        grid = parse(file_input)
        risk_level, low_points = partOne(grid)
        print(f"Part 1: {risk_level}")
        print(f"Part 2: {partTwo(grid, low_points)}")

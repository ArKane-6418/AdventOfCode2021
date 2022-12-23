from typing import List
import sys
import numpy as np

def parse(file_input: str) -> np.ndarray:
    result = file_input.strip().split("\n")
    for i in range(len(result)):
        result[i] = list(map(int, list(result[i])))
    return np.array(result)


def get_neighbours(grid: np.ndarray, row: int, col: int) -> List[List[int]]:
    dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    rows = len(grid)
    cols = len(grid[0])
    neighbours = []

    for dr, dc in dirs:
        r = row + dr
        c = col + dc

        if r in range(rows) and c in range(cols):
            neighbours.append([r, c])

    return neighbours


def solution(grid: np.ndarray) -> List[int]:
    steps = 0
    rows = len(grid)
    cols = len(grid[0])
    partOne = 0
    partTwo = 0

    while True:
        flashes = 0
        flashed = []
        steps += 1
        grid += 1
        find_flashes = np.where(grid > 9)
        coordinates_list = list(zip(find_flashes[0], find_flashes[1]))
        for coordinates in coordinates_list:
            grid[coordinates[0], coordinates[1]] = 0
            flashed.append(coordinates)

        while flashed:
            row, col = flashed.pop()
            flashes += 1
            # Add 1 to every coordinate in the 8 cardinal directions if
            # possible
            for new_row, new_col in get_neighbours(grid, row, col):
                # If we see a 0, we know an octopus just flashed so we should
                # ignore it
                if grid[new_row, new_col] == 0:
                    continue

                grid[new_row, new_col] += 1

                if grid[new_row, new_col] > 9:
                    grid[new_row, new_col] = 0
                    flashed.append((new_row, new_col))

        if steps <= 100:
            partOne += flashes
        if flashes == rows * cols:
            partTwo = steps
            break

    return [partOne, partTwo]


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        file_input = f.read()
        grid = parse(file_input)
        sol = solution(grid)
        print(f"Part 1: {sol[0]}")
        print(f"Part 2: {sol[1]}")

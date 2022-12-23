import numpy as np
with open("input03.txt", "r") as f:
    lines = [list(line.strip()) for line in f]
    print(lines)
    grid = np.array(lines, dtype=int)
    num, width = np.shape(grid)

    # ---------- Part 1 ----------

    def mostCommonDigit(column):
        num_ones = sum(grid[:,column] == 1)
        return '1' if num_ones >= np.shape(grid)[0] // 2 else '0'

    gammaDigits = [mostCommonDigit(column) for column in range(width)]
    epsilonDigits = ['1' if digit == '0' else '0' for digit in gammaDigits]
    gamma = int(''.join(gammaDigits), 2)
    epsilon = int(''.join(epsilonDigits), 2)
    print(f"Part 1: {gamma * epsilon}")

    # ---------- Part 2 ----------

    def filterMostCommon(grid, column):
        num_ones = sum(grid[:,column] == 1)
        num_zeros = sum(grid[:,column] == 0)
        most_common = 1 if num_ones >= num_zeros else 0
        return np.delete(grid, np.where(grid[:,column] != most_common)[0], axis=0)

    def filterLeastCommon(grid, column):
        num_ones = sum(grid[:,column] == 1)
        num_zeros = sum(grid[:,column] == 0)
        least_common = 0 if num_zeros <= num_ones else 1
        return np.delete(grid, np.where(grid[:,column] != least_common)[0], axis=0)

    grid = np.array(lines, dtype=int)
    column = 0
    while np.shape(grid)[0] > 1:
        grid = filterMostCommon(grid, column)
        column += 1

    oxy_gen = int(''.join([str(grid[0, i]) for i in range(width)]), 2)

    grid = np.array(lines, dtype=int)
    column = 0
    while np.shape(grid)[0] > 1:
        grid = filterLeastCommon(grid, column)
        column += 1

    CO2_scrub = int(''.join([str(grid[0, i]) for i in range(width)]), 2)

    print(f"Part 2: {oxy_gen * CO2_scrub}")

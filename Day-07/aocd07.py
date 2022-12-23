from typing import List
import sys

def partOne(challenge_input: List[int]) -> int:
    sums = []
    for i in range(min(challenge_input), max(challenge_input)+1):
        # Add up all the differences between each crab's current position and
        # the proposed position
        s = sum([abs(n-i) for n in challenge_input])
        sums.append(s)
    return min(sums)

def partTwo(challenge_input: List[int]) -> int:
    sums = []
    for i in range(min(challenge_input), max(challenge_input)+1):
        # Now, the fuel cost is the arithmetic sum from 1 to the difference between each crab's current position and
        # the proposed position
        s = sum([(abs(n-i) * (abs(n-i)+1)) // 2 for n in challenge_input])
        sums.append(s)
    return min(sums)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        file_input = list(map(int, f.read().split(",")))
        print(f"Part 1: {partOne(file_input)}")
        print(f"Part 2: {partTwo(file_input)}")


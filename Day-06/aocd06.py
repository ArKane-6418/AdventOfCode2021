from typing import List
from collections import defaultdict
import sys

def compute_population(challenge_input: List[int], days: int) -> int:
    # Create dictionary for calculating the number of births on a given day
    num_births = defaultdict(lambda: 0)
    population = len(challenge_input)
    for d in challenge_input:
        # If a lanternfish has an internal timer of 2, that means they will
        # give birth on day 3
        num_births[d+1] += 1

    for day in range(1, days+1):
        # The number of lanternfish giving birth is equal to the number of
        # lanternfish born
        births = num_births[day]
        # Only update the population and dict when there are births on that day
        if births > 0:
            population += births
            # The lanternfish that gave birth on this day will next give birth
            # 7 days later
            num_births[day+7] += births
            # The lanternfish that were born will give birth 9 days later on
            # their first cycle
            num_births[day+9] += births

    return population

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        file_input = list(map(int, f.read().split(",")))
        print(f"Part 1: {compute_population(file_input, 80)}")
        print(f"Part 2: {compute_population(file_input, 256)}")

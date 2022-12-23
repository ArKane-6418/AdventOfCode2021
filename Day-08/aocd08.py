from typing import List, Tuple, Set
import sys

def parse(file_input: str) -> Tuple[List[List[str]], List[List[str]]]:
    lines = file_input.strip().split("\n")
    left, right = [], []
    for line in lines:
        patterns, output = line.split(" | ")
        left.append(patterns.split(" "))
        right.append(output.split(" "))

    return left, right

def partOne(challenge_input: List[List[str]]) -> int:
    count = 0
    for line in challenge_input:
        for i in range(4):
            if len(line[i]) in [2, 3, 4, 7]:
                count += 1

    return count


def get_difference(s1: str, s2: str) -> str:
    # Want to be able to map a letter to another letter which is why we only
    # want one element not shared between two signals
    difference = set(s1) - set(s2)
    assert len(difference) == 1
    return list(difference)[0]


def get_common(s1: str, s2: str) -> str:
    # Want to be able to map a letter to another letter which is why we only
    # want one element shared between two signals
    intersection = set(s1).intersection(set(s2))
    assert len(intersection) == 1
    return list(intersection)[0]


def get_signals_by_length(input_row: List[str], length: int) -> List[str]:
    return list(filter(lambda x: len(x) == length, input_row))


def filter_shared_letters(candidates: List[str], letters: List[str]) -> str:
    # We want to ensure there is only one candidate pattern left
    result = list(filter(lambda x: set(letters).issubset(set(x)), candidates))
    assert len(result) == 1
    return result[0]


def filter_unshared_letters(candidates: List[str], letters: List[str]) -> str:
    # We want to ensure there is only one candidate pattern left
    result = list(filter(lambda x: not set(letters).issubset(set(x)), candidates))
    assert len(result) == 1
    return result[0]


def decode_signal(pattern: List[str]) -> List[Set[str]]:
    digits = {}
    # Map each letter from the original to its counterpart
    segments = {}

    digits[1] = get_signals_by_length(pattern, 2)[0]
    digits[4] = get_signals_by_length(pattern, 4)[0]
    digits[7] = get_signals_by_length(pattern, 3)[0]
    digits[8] = get_signals_by_length(pattern, 7)[0]

    # The only difference ebtween 7 and 1 is the top line, which corresponds to
    # a
    segments["a"] = get_difference(digits[7], digits[1])

    # Now that we have 1, we look at the digits with 6 letters, 0, 6, and 9
    # Note that 6 is the only number of the three that doesn't contain the
    # segments of 1

    six_segments = get_signals_by_length(pattern, 6)
    digits[6] = filter_unshared_letters(six_segments, list(digits[1]))
    # 6 contains f but not c so we compare it with 1 to find the
    # mapping of c and f
    segments["c"] = get_difference(digits[1], digits[6])
    segments["f"] = get_common(digits[1], digits[6])

    six_segments.remove(digits[6])

    # 2, 3, and 5 all have 5 segments but only 3 contains 1
    five_segments = get_signals_by_length(pattern, 5)

    digits[3] = filter_shared_letters(five_segments, list(digits[1]))
    five_segments.remove(digits[3])

    # Out of 0 and 9, 9 contains 3 so we can filter 0 out
    digits[9] = filter_shared_letters(six_segments, list(digits[3]))
    six_segments.remove(digits[9])
    digits[0] = six_segments[0]

    # Now that we have 9, we can it and 3 to get the letter corresponding to b
    segments["b"] = get_difference(digits[9], digits[3])

    # We can use 0 and 8 to get the letter corresponding to d
    segments["d"] = get_difference(digits[8], digits[0])

    # We can use 9 and 8 to get the letter corresponding to e
    segments["e"] = get_difference(digits[8], digits[9])

    # Out of 2 and 5, only 5 contains b
    digits[5] = filter_shared_letters(five_segments, [segments["b"]])
    five_segments.remove(digits[5])

    digits[2] = five_segments[0]

    segments["g"] = get_difference(digits[8], digits[4] + segments["a"] +
                                   segments["e"])

    result = []

    for i in range(10):
        result.append(set(digits[i]))

    return result


def partTwo(left: List[List[str]], right: List[List[str]]) -> int:
    result = 0

    for i in range(len(left)):
        decoded = decode_signal(left[i])
        n = 0
        for signal in right[i]:
            n = (10 * n) + decoded.index(set(signal))
        result += n

    return result


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        file_input = f.read()
        patterns, output = parse(file_input)
        print(f"Part 1: {partOne(output)}")
        print(f"Part 2: {partTwo(patterns, output)}")

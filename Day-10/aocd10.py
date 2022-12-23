from typing import List
import sys

def parse(file_input: str) -> List[List[str]]:
    return file_input.strip().split("\n")


def partOne(lines: List[List[str]]) -> int:
    matches = {")": "(", "]": "[", "}": "{", ">": "<"}
    score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
    lines_to_discard = []
    score = 0

    for line in lines:
        stack = []

        for bracket in line:
            if bracket in matches.values():
                stack.append(bracket)
            # We have a closing bracket in this case
            else:
                if matches[bracket] == stack[-1]:
                    stack.pop()
                else:
                    score += score_map[bracket]
                    lines_to_discard.append(line)
                    # Once we find an illegal bracket, we're done, go to
                    # next line
                    break

    return score, lines_to_discard


def partTwo(lines: List[List[str]]) -> int:
    matches = {")": "(", "]": "[", "}": "{", ">": "<"}
    reverse_matches = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score_map = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []

    for line in lines:
        score = 0
        stack = []

        for bracket in line:
            if bracket in matches.values():
                stack.append(bracket)
            else:
                if matches[bracket] == stack[-1]:
                    stack.pop()
        # Iterate through what's left of the stack in reverse
        for i in range(len(stack)-1, -1, -1):
            closing_bracket = reverse_matches[stack[i]]
            score = score * 5 + score_map[closing_bracket]
        scores.append(score)

    scores.sort()

    return scores[len(scores) // 2]


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        file_input = f.read()
        lines = parse(file_input)
        p1_score, lines_to_discard = partOne(lines)
        print(f"Part 1: {p1_score}")

        for line in lines_to_discard:
            lines.remove(line)

        print(f"Part 2: {partTwo(lines)}")

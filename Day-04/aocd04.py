from typing import List, Tuple

class BingoBoard:
    def __init__(self, input_string: str) -> None:
        self.is_bingo = False
        self.rows = [set() for _ in range(5)]
        self.cols = [set() for _ in range(5)]
        lines = input_string.split("\n")
        # Convert each list of strings into list of itns
        # Assume 5 x 5 board
        for r in range(5):
            num_row = list(map(int, lines[r].split()))
            for c in range(5):
                # Add each number to the respective row and columns
                self.rows[r].add(num_row[c])
                self.cols[c].add(num_row[c])

    def play(self, num: int) -> bool:
        # Iterate through the rows and colums to remove the number
        for i in range(5):
            self.rows[i].discard(num)
            self.cols[i].discard(num)

            # There is a bingo when a row or column is complete
            if len(self.rows[i]) == 0 or len(self.cols[i]) == 0:
                self.is_bingo = True

        return self.is_bingo

    def compute_sum(self):
        return sum([sum(self.rows[i]) for i in range(5)])


def parse_boards(file_input: List[str]) -> Tuple[List[int], List[BingoBoard]]:
    nums = list(map(int, file_input[0].split(",")))
    boards = []
    board_input = file_input[1::]

    for board in board_input:
        boards.append(BingoBoard(board))

    return nums, boards

def partOne(nums: List[int], boards: List[BingoBoard]) -> int:
    for num in nums:
        for board in boards:
            if board.play(num):
                return num * board.compute_sum()


def partTwo(nums: List[int], boards: List[BingoBoard]) -> int:
    last_winner = None
    for num in nums:
        for board in boards:
            # This time, check if the board already has a bingo, and if so,
            # skip it
            if board.is_bingo:
                continue
            if board.play(num):
                last_winner = num * board.compute_sum()
    return last_winner

if __name__ == "__main__":
    with open("input04.txt") as f:
        # Read the sequence of numbers
        file_input = f.read().split("\n\n")
        nums, boards = parse_boards(file_input)
        print(f"Part 1: {partOne(nums, boards)}")
        print(f"Part 2: {partTwo(nums, boards)}")

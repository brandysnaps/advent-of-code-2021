from itertools import chain, compress
import numpy as np
import sys

class BingoBoard:
    def __init__(self, index: int, board: list):
        self.index = index
        self.board = board
        self.board_filter = [False for _ in range(len(self.board))]


    def check_number(self, number: int) -> None:
        try:
            index = self.board.index(number)
        except ValueError:
            return

        self.board_filter[index] = True


    def check_win_condition(self) -> bool:
        # Split list
        board = np.array(self.board_filter).reshape((5, 5))

        if np.all(board, axis=0).any() or np.all(board, axis=1).any():
            return True

        return False

    def calculate_win_score(self, number: int) -> int:
        board_filter = [not i for i in self.board_filter]
        unmarked_numbers = list(compress(self.board, board_filter))
        score = number * sum(unmarked_numbers)
        return score


def process_input(input: list) -> list:
    numbers = input[0].split(",")

    rows = [row.split() for row in input[1:] if row]
    single_row =  list(chain.from_iterable(rows))
    single_row_numbers = [int(i) for i in single_row]
    boards = [single_row_numbers[x:x+5*5] for x in range(0, len(single_row_numbers), 5*5)]

    return numbers, boards


with open("input", "r") as file:
    numbers, boards = process_input(file.read().split("\n"))

bingo_boards = []

# Create instances of bingo boards
for index, board in enumerate(boards, start=1):
    bingo_boards.append(BingoBoard(index, board))

for number in numbers:
    for bingo_board in bingo_boards:
        if len(bingo_boards) == 1:
            sys.exit()

        bingo_board.check_number(int(number))
        if bingo_board.check_win_condition():
            print(f"Board {bingo_board.index} wins!")
            print(bingo_board.calculate_win_score(int(number)))
            bingo_boards.remove(bingo_board)

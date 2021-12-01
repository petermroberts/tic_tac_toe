
from board import *

class Player:

    def __init__(self, name, marker) -> None:
        self.name = name
        self.marker = marker
        self.wins = 0
        self.roll = 0

    def choose_position(self, board):
        try:
            chosen_position = int(input(f"{self.name} please choose where you want to place your marker (1-9): "))
            if board.check_position(chosen_position):
                raise PositionTakenError
            if not 0 <= chosen_position <= 8:
                raise PositionOutOfBoundsError

        except PositionTakenError:
            return self.choose_position(board)

        except PositionOutOfBoundsError:
            return self.choose_position(board)

        else:
            return chosen_position
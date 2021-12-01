
from board import *

class Player:

    def __init__(self, name, marker) -> None:
        self.name = name
        self.marker = marker
        self.wins = 0
        self.roll = 0
        
    def take_turn(self, board):
        self.select_position(board)
        board.print_board()

    def select_position(self, board):
        chosen_position = self.choose_position(board)
        board.place_marker(chosen_position, self.marker)

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
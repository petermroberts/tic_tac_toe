
from board import *

class Player:

    def __init__(self, name, marker) -> None:
        self.name = name
        self.marker = marker
        self.wins = 0
        self.roll = 0
    
    # Func to run the turn sequence
    def take_turn(self, board):
        self.select_position(board)
        board.print_board()

    # Func to call the user to choose a position
    def select_position(self, board):
        chosen_position = self.choose_position(board) # Gives a valid position
        board.place_marker(chosen_position, self.marker) # Places the marker

    def choose_position(self, board):
        try:
            chosen_position = int(input(f"{self.name} please choose where you want to place your marker (1-9): "))
            if not 0 <= chosen_position <= 8:
                raise PositionChosenError(chosen_position, "02")
            if board.check_position(chosen_position):
                raise PositionChosenError(chosen_position, "01")

        except PositionChosenError as e:
            print(e)
            return self.choose_position(board)

        else:
            return chosen_position
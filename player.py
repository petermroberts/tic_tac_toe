
from game_master import *
from main import choose_first_turn

class Player:

    def __init__(self, name, marker) -> None:
        self.name = name
        self.marker = marker
        self.wins = 0
        self.roll = 0

    def choose_position(self, game_master):
        try:
            chosen_position = int(input(f"{self.name} please choose where you want to place your marker (1-9): ")) - 1
            if game_master.check_postion(chosen_position):
                raise PositionError("Position already filled, please choose again")
            if chosen_position > 8 or chosen_position < 0:
                raise PositionError("Position out of bounds")

        except PositionError:
            self.choose_position()

        finally:
            return chosen_position
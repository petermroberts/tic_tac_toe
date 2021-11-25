
from game_master import GameMaster

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
                raise PositionException("Position already filled, please choose again: ")
        except PositionException:
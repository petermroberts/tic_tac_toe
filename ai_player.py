
from player import Player

class ai_player(Player):
    def __init__(self) -> None:
        super().__init__()

    # Todo: find a way for the ai to easily tell if the user is going to win next move
    def choose_position(self, board):
        return super().choose_position(board)
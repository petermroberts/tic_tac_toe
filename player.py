
class Player:

    def __init__(self, name, marker) -> None:
        self.name = name
        self.marker = marker
        self.wins = 0
        self.roll = 0
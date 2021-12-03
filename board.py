
class Board:

    convert_dict = {0: ' ', 1: 'X', 2: 'O'}
    def __init__(self):
        self.board = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.game_over = False

    def place_marker(self, position, marker):
        self.board[position] = marker

    def check_position(self, position):
        if self.board[position] != 0:
            return True
        else: return False

    def print_board(self):
        x, y, z = 1, 2, 3
        for i in range(3):
            print("     |     |     ")
            print(f"  {self.convert_dict[self.board[x]]}  |  {self.convert_dict[self.board[y]]}  |  {self.convert_dict[self.board[z]]}  ")
            print("     |     |     ")
            x += 3
            y += 3
            z += 3
            if i != 2:
                print("-----------------")

    def check_win(self):

        if self.board[1] == self.board[2] == self.board[3] != 0:
            self.game_over = True
            return self.convert_dict[self.board[1]]

        elif self.board[4] == self.board[5] == self.board[6] != 0:
            self.game_over = True
            return self.convert_dict[self.board[4]]

        elif self.board[7] == self.board[8] == self.board[9] != 0:
            self.game_over = True
            return self.convert_dict[self.board[7]]

        elif self.board[1] == self.board[5] == self.board[9] != 0:
            self.game_over = True
            return self.convert_dict[self.board[1]]

        elif self.board[3] == self.board[5] == self.board[7] != 0:
            self.game_over = True
            return self.convert_dict[self.board[3]]

        elif self.board[1] == self.board[4] == self.board[7] != 0:
            self.game_over = True
            return self.convert_dict[self.board[1]]

        elif self.board[2] == self.board[5] == self.board[8] != 0:
            self.game_over = True
            return self.convert_dict[self.board[1]]

        elif self.board[3] == self.board[6] == self.board[9] != 0:
            self.game_over = True
            return self.convert_dict[self.board[2]]

        else:
            return None

class PositionChosenError(Exception):
    '''Exception raised when player chooses a position already filled'''
    def __init__(self, position, error_token, message="PositionChosenError"):
        self.position = position
        self.message = message
        self.error_token = error_token
        self.errors = {
            "01": "already chosen",
            "02": "not on the board"
        }
        super().__init__(self.message)

    def __str__(self):
        return f'Position {self.position} is {self.errors[self.error_token]}, please choose another position: '

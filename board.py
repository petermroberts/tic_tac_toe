
class Board:

    numToStr = {0: ' ', 1: 'X', 2: 'O'} # This dict is to convert numbers on the board into strings

    def __init__(self):
        # Game board, used ints to reduce complexity
        self.board = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.game_over = False # To determine if there was a winner

    def place_marker(self, position, marker):
        self.board[position] = marker # Place the users marker

    # Func to determine if the chosen position has already been filled
    def check_position(self, position):
        if self.board[position] != 0:
            return True
        else: return False

    # Func to print tictactoe board
    def print_board(self):
        pos_list = [1, 4, 7]
        for pos in pos_list:
            print("     |     |     ")
            print(f"  {self.numToStr[self.board[pos]]}  |  {self.numToStr[self.board[pos+1]]}  |  {self.numToStr[self.board[pos+2]]}  ")
            print("     |     |     ")
            if pos != 7:
                print("-----------------")

    # Func to check if someone won
    def check_win(self):

        if self.board[1] == self.board[2] == self.board[3] != 0:
            self.game_over = True

        elif self.board[4] == self.board[5] == self.board[6] != 0:
            self.game_over = True

        elif self.board[7] == self.board[8] == self.board[9] != 0:
            self.game_over = True

        elif self.board[1] == self.board[5] == self.board[9] != 0:
            self.game_over = True

        elif self.board[3] == self.board[5] == self.board[7] != 0:
            self.game_over = True

        elif self.board[1] == self.board[4] == self.board[7] != 0:
            self.game_over = True

        elif self.board[2] == self.board[5] == self.board[8] != 0:
            self.game_over = True

        elif self.board[3] == self.board[6] == self.board[9] != 0:
            self.game_over = True

        if self.game_over == True:
            return True
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


class GameMaster:

    def __init__(self):
        self.board = [0, 0, 0,
                      0, 0, 0,
                      0, 0, 0]
        self.game_over = False

    def place_marker(self, position, marker):
        self.board[position] = marker

    def check_position(self, position):
        if self.board[position] != 0:
            return True
        return False

    def print_board(self):
        x, y, z = 0, 1, 2
        convert_dict = {0: " ", 1: "X", 2: "O"}
        for i in range(3):
            print("     |     |     ")
            print(f"  {convert_dict[self.board[x]]}  |  {convert_dict[self.board[y]]}  |  {convert_dict[self.board[z]]}  ")
            print("     |     |     ")
            x += 3
            y += 3
            z += 3
            if i != 2:
                print("-----------------")

    def check_win(self):

        if self.board[0] == self.board[1] == self.board[2] != 0:
            self.game_over = True
            return self.board[0]

        elif self.board[3] == self.board[4] == self.board[5] != 0:
            self.game_over = True
            return self.board[3]

        elif self.board[6] == self.board[7] == self.board[8] != 0:
            self.game_over = True
            return self.board[6]

        elif self.board[0] == self.board[4] == self.board[8] != 0:
            self.game_over = True
            return self.board[0]

        elif self.board[2] == self.board[4] == self.board[6] != 0:
            self.game_over = True
            return self.board[0]

        elif self.board[0] == self.board[3] == self.board[6] != 0:
            self.game_over = True
            return self.board[0]

        elif self.board[1] == self.board[4] == self.board[7] != 0:
            self.game_over = True
            return self.board[1]

        elif self.board[2] == self.board[5] == self.board[8] != 0:
            self.game_over = True
            return self.board[2]

        else:
            return None

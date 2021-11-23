from game_master import GameMaster

def select_position(game_master):
    chosen_position = int(input("Please choose where you want to place your marker (1-9)")) - 1
    while game_master.check_position(chosen_position):
        int(input("That position is already filled, please choose again"))
    game_master.place_marker(chosen_position)

def main():

    game_master = GameMaster()

    print("Welcome to tic tac toe!\n")
    if input("Would you like to be X or O?").casefold == "x":
        game_master.player1_marker = 1
        game_master.player2_marker = 2
    else:
        game_master.player1_marker = 2
        game_master.player2_marker = 1

    while not game_master.game_over:
        game_master.print_board()
        select_position()

if __name__ == "__main__":
    main()
from game_master import GameMaster
from player import Player
import random

def roll_die(player):
    player.roll = random.randint(1,6)

def choose_first_turn(player1, player2):
    roll_die(player1)
    roll_die(player2)
    if player1.roll > player2.roll:
        return [player1, player2]
    else:
        return [player2, player1]

def select_position(game_master, player):
    chosen_position = int(input("Please choose where you want to place your marker (1-9)")) - 1
    while game_master.check_position(chosen_position):
        int(input("That position is already filled, please choose again"))
    game_master.place_marker(chosen_position, player.marker)

def main():

    game_master = GameMaster()

    print("Welcome to tic tac toe!\n")
    if input("Would you like to be X or O?").casefold == "x":
        player1 = Player(1)
        player2 = Player(2)
    else:
        player1 = Player(2)
        player2 = Player(1)

    players = choose_first_turn(player1, player2)

    while not game_master.game_over:
        for player in players:
            select_position(game_master, player)
            game_master.print_board()
            print(f"{game_master.check_win()} won!")

if __name__ == "__main__":
    main()
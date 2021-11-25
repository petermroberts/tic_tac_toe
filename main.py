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
    
    while game_master.check_position(chosen_position):
        chosen_position = int(input("That position is already filled, please choose again: ")) - 1
    game_master.place_marker(chosen_position, player.marker)

def main():

    game_master = GameMaster()

    print("Welcome to tic tac toe!\n")
    if input("Would you like to be X or O? ").casefold == "x":
        player1 = Player("Player 1", 1)
        player2 = Player("Player 2", 2)
    else:
        player1 = Player("Player 1", 2)
        player2 = Player("Player 2", 1)

    players = choose_first_turn(player1, player2)

    while not game_master.game_over:
        for player in players:
            game_master.print_board()
            select_position(game_master, player)
            if game_master.check_win():
                print(f"{game_master.check_win()} won!")
        game_master.print_board()

if __name__ == "__main__":
    main()
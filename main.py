from game_master import GameMaster
from player import Player
import random

def create_players():
    if input("Would you like to be X or O? ").casefold == "x":
        return choose_first_turn(Player("Player 1", 1), Player("Player 2", 2))
    else:
        return choose_first_turn(Player("Player 1", 2), Player("Player 2", 1))

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
    chosen_position = int(input(f"{player.name} please choose where you want to place your marker (1-9): ")) - 1
    while game_master.check_position(chosen_position):
        chosen_position = int(input("That position is already filled, please choose again: "))
    game_master.place_marker(chosen_position, player.marker)

def main():

    game_master = GameMaster()

    print("Welcome to tic tac toe!\n")
    players = create_players()

    while not game_master.game_over:
        for player in players:
            select_position(game_master, player)
            game_master.print_board()
            if game_master.check_win():
                print(f"{game_master.check_win()} won!")

if __name__ == "__main__":
    main()
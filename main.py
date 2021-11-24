from game_master import GameMaster
from player import Player
import random

# Fuction to create player obects and assign them markers
def create_players():
    # Before sending list of player objects, randomize who goes first
    if input("Would you like to be X or O? ").casefold() == "x": # If the user chose to play as x, assign o to other player
        return choose_first_turn(Player("Player 1", 1), Player("Player 2", 2))
    else:
        return choose_first_turn(Player("Player 1", 2), Player("Player 2", 1))

# Function to roll a die
def roll_die(player):
    player.roll = random.randint(1,6)

# Function to determine the order of play
def choose_first_turn(player1, player2):
    roll_die(player1)   # Call roll_die function to determine who goes first
    roll_die(player2)
    if player1.roll > player2.roll: # Highest roll goes first
        return [player1, player2]
    else:
        return [player2, player1]

# Function to determine where to place marker
def select_position(game_master, player):
    chosen_position = int(input(f"{player.name} please choose where you want to place your marker (1-9): ")) - 1
    while game_master.check_position(chosen_position):  # If the position is already chosen, ask for another position
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
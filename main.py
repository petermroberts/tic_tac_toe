from board import Board
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

def main():

    board = Board()

    print("Welcome to tic tac toe!\n")
    players = create_players()

    while not board.game_over:
        for player in players:
            player.take_turn(board)
            if board.check_win():
                print(f"{board.check_win()} won!")
                break

if __name__ == "__main__":
    main()
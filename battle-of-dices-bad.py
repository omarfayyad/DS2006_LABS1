# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D6.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Recursive function to handle rounds
def play_round(player1_wins, player2_wins):
    # Generate dice rolls each round
    input("\nPress ENTER to roll the dice...")
    player1_roll = random.randint(1, 6)
    player2_roll = random.randint(1, 6)

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    input("\nPress ENTER to continue...")

    # Check winner of this round
    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because", player1_roll, "is greater than", player2_roll)
    elif player1_roll == player2_roll:
        print("Amaaazzinng! This round has a tie!")
    else:
        player2_wins += 1
        print("Player 2 wins this round!")
        print("Because", player2_roll, "is greater than", player1_roll)

    # Print score
    print("The game score is Player 1", player1_wins, "vs.", player2_wins, "Player 2.")

    # Check if the game has a winner
    if player1_wins == 3:
        print("🏆 Player 1 is the top #1 Player in Battle of Dices!")
    elif player2_wins == 3:
        print("🏆 Player 2 is the top #1 Player in Battle of Dices!")
    else:
        print("🔥 This heated Battle of Dices isn't ending! Who will win in the end?!")
        play_round(player1_wins, player2_wins)  # recursive call!


# Start the game with 0 wins each
play_round(0, 0)

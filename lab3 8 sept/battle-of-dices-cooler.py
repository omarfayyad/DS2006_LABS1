import random
from dice import rollD6, rollD8  # Import the dice functions

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
round_number = 1  # Track number of rounds played

# Keep playing until one player reaches 3 wins
while player1_wins < 3 and player2_wins < 3:
    print(f"\n--- Round {round_number} ---")
    input("Press ENTER to roll the dice...")

    # Player 1 rolls two dice
    player1_roll1 = rollD6()
    player1_roll2 = rollD8()
    player1_sum = player1_roll1 + player1_roll2

    # Player 2 rolls two dice
    player2_roll1 = rollD6()
    player2_roll2 = rollD8()
    player2_sum = player2_roll1 + player2_roll2

    print(f"Player 1 rolled {player1_roll1} (d6) + {player1_roll2} (d8) = {player1_sum}")
    print(f"Player 2 rolled {player2_roll1} (d6) + {player2_roll2} (d8) = {player2_sum}")

    # Determine round winner
    if player1_sum > player2_sum:
        player1_wins += 1
        print("Player 1 wins this round!")
    elif player2_sum > player1_sum:
        player2_wins += 1
        print("Player 2 wins this round!")
    else:
        print("Amaaazzinng! This round has a tie!")

    # Print the game score
    print("The game score is Player 1", player1_wins, "vs.", player2_wins, "Player 2.")

    round_number += 1  # Next round

# Announce the game winner
if player1_wins == 3:
    print("\n🏆 Player 1 is the top #1 Player in Battle of Dices!")
else:
    print("\n🏆 Player 2 is the top #1 Player in Battle of Dices!")

print("It took", round_number - 1, "rounds to win the game.")
print("🔥 This heated Battle of Dices has ended!")

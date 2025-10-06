import random
from dice import rollD6  # Import the dice function you created

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
round_number = 1  # Track number of rounds played

# Keep playing until one player reaches 3 wins
while player1_wins < 3 and player2_wins < 3:
    print(f"\n--- Round {round_number} ---")
    input("Press ENTER to roll the dice...")

    # Use rollD6() instead of random.randint
    player1_roll = rollD6()
    player2_roll = rollD6()

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

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

    # Print the game score:
    print("The game score is Player 1", player1_wins, "vs.", player2_wins, "Player 2.")

    round_number += 1  # Next round

# Now we need to check who won.
if player1_wins == 3:
    print("\n🏆 Player 1 is the top #1 Player in Battle of Dices!")
    print("It took", round_number - 1, "rounds to win the game.")
else:
    print("\n🏆 Player 2 is the top #1 Player in Battle of Dices!")
    print("It took", round_number - 1, "rounds to win the game.")
print("🔥 This heated Battle of Dices has ended!")
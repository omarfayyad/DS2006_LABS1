import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Recursive function to handle rounds
def play_round(round_number, player1_wins, player2_wins, player1_history, player2_history):
    print(f"\n Round {round_number} ")
    input("\nPress ENTER to roll the dice...")

    # Dice rolls
    player1_roll = random.randint(1, 6)
    player2_roll = random.randint(1, 6)

    # Save history
    player1_history.append(player1_roll)
    player2_history.append(player2_roll)

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    input("\nPress ENTER to continue...")

    # Check winner of this round
    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
    elif player1_roll == player2_roll:
        print("Amaaazzinng! This round has a tie!")
    else:
        player2_wins += 1
        print("Player 2 wins this round!")

    # Print score
    print("The game score is Player 1", player1_wins, "vs.", player2_wins, "Player 2.")

    # Check if the game has a winner
    if player1_wins == 3:
        print("\n🏆 Player 1 is the top #1 Player in Battle of Dices!")
        show_history(player1_history, player2_history)
    elif player2_wins == 3:
        print("\n🏆 Player 2 is the top #1 Player in Battle of Dices!")
        show_history(player1_history, player2_history)
    else:
        play_round(round_number + 1, player1_wins, player2_wins, player1_history, player2_history)

# Function to display the history table
def show_history(player1_history, player2_history):
    rounds = len(player1_history)

    print("\n-----------------------------------------")
    # Round numbers
    print("| Round    |", " | ".join(str(i+1) for i in range(rounds)), "|")
    print("-----------------------------------------")
    # Player 1 rolls
    print("| Player 1 |", " | ".join(str(r) for r in player1_history), "|")
    print("-----------------------------------------")
    # Player 2 rolls
    print("| Player 2 |", " | ".join(str(r) for r in player2_history), "|")
    print("-----------------------------------------")

# Start the game with 0 wins each and empty histories
play_round(1, 0, 0, [], [])

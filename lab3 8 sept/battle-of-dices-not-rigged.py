import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Recursive function to handle rounds
def play_round(round_number, player1_wins, player2_wins, player1_rolls, player2_rolls):
    print(f"\n Round {round_number} ")
    input("\nPress ENTER to roll the dice for Player 1...")
    player1_roll = random.randint(1, 6)
    print("Player 1 rolled:", player1_roll)
    player1_rolls.append(player1_roll)  # Store the roll

    input("Press ENTER to roll the dice for Player 2...")
    player2_roll = random.randint(1, 6)
    print("Player 2 rolled:", player2_roll)
    player2_rolls.append(player2_roll)  # Store the roll

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
    print(f"The game score is Player 1 {player1_wins} vs. {player2_wins} Player 2.")

    # Check if the game has a winner
    if player1_wins == 3:
        print("\n🏆 Player 1 is the top #1 Player in Battle of Dices!")
        save_history(player1_rolls, player2_rolls)
    elif player2_wins == 3:
        print("\n🏆 Player 2 is the top #1 Player in Battle of Dices!")
        save_history(player1_rolls, player2_rolls)
    else:
        play_round(round_number + 1, player1_wins, player2_wins, player1_rolls, player2_rolls)

# Function to display and save the history table
def save_history(player1_rolls, player2_rolls):
    rounds = len(player1_rolls)
    
    # Build the table as a string
    table_lines = []
    table_lines.append("\n🎲 Game Summary 🎲")
    table_lines.append("-" * 40)
    table_lines.append(f"{'Round':<6} {'Player 1':<10} {'Player 2':<10} {'Dice':<6}")
    table_lines.append("-" * 40)
    
    for i in range(rounds):
        table_lines.append(f"{i+1:<6} {player1_rolls[i]:<10} {player2_rolls[i]:<10} {'D6':<6}")
    
    table_lines.append("-" * 40)
    
    # Print the table to console
    for line in table_lines:
        print(line)
    
    # Ask user for filename
    filename = input("\nEnter the name of the file to save the game summary (e.g., summary.txt): ")
    
    # Save the table to the file
    with open(filename, "w") as f:
        for line in table_lines:
            f.write(line + "\n")
    
    print(f"Game summary saved to {filename} ✅")

# Start the game
play_round(1, 0, 0, [], [])
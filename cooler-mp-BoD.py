# cooler-multiplayer-battle-of-dices.py

import random
from dice import rollD6, rollD8  # Import the dice functions

WINNING_SCORE = 3  # Number of wins needed to win the game

print("🎲 Welcome to the Multiplayer Battle of Dices! 🎲")

# Get number of players
num_players = int(input("Enter number of players: "))

# Get player names
player_names = []
for i in range(num_players):
    name = input(f"Enter name for Player {i+1}: ")
    player_names.append(name)

# Initialize scores and histories
player_wins = [0] * num_players
player_rolls_history = [[] for _ in range(num_players)]

round_number = 1
game_over = False

# Game loop
while not game_over:
    print(f"\n--- Round {round_number} ---")
    input("Press ENTER to roll the dice...")

    # Each player rolls 1 d6 and 1 d8
    round_rolls = []
    for i, name in enumerate(player_names):
        roll1 = rollD6()
        roll2 = rollD8()
        total = roll1 + roll2
        round_rolls.append(total)
        player_rolls_history[i].append(total)
        print(f"{name} rolled {roll1} (d6) + {roll2} (d8) = {total}")

    # Determine round winner(s)
    highest_score = max(round_rolls)
    winners = [i for i, score in enumerate(round_rolls) if score == highest_score]

    if len(winners) == 1:
        winner_index = winners[0]
        player_wins[winner_index] += 1
        print(f"🏆 {player_names[winner_index]} wins this round!")
    else:
        tied_names = ", ".join(player_names[i] for i in winners)
        print(f"🤝 It's a tie between: {tied_names}. No points this round.")

    # Print current scoreboard
    scoreboard = " | ".join([f"{player_names[i]}: {player_wins[i]} wins" for i in range(num_players)])
    print("📊 Current Scoreboard:", scoreboard)

    # Check if someone won the game
    for i in range(num_players):
        if player_wins[i] >= WINNING_SCORE:
            print(f"\n🏆 {player_names[i]} is the champion of Battle of Dices with {player_wins[i]} wins!")
            print(f"🔥 The battle lasted {round_number} rounds!")
            game_over = True
            break

    round_number += 1
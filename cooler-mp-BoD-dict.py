# cooler-multiplayer-battle-of-dices-dict.py

import random
import copy
from dice import rollD6, rollD8  # Import dice functions

WINNING_SCORE = 3  # Number of wins needed to win the game

# Dictionary template for storing player information
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": [],   # history of total rolls per round
}

# List to store the dicts for each player
players = []

print("🎲 Welcome to the Cooler Multiplayer Battle of Dices! 🎲")

# Number of players
num_players = int(input("Enter number of players: "))

# Gather player info
for i in range(num_players):
    player = copy.deepcopy(player_info)
    player["name"] = input(f"Enter name for Player {i+1}: ")
    player["email"] = input(f"Enter email for Player {i+1}: ")
    player["country"] = input(f"Enter country for Player {i+1}: ")
    players.append(player)

round_number = 1
game_over = False

# Game loop
while not game_over:
    print(f"\n--- Round {round_number} ---")
    input("Press ENTER to roll the dice...")

    # Dice rolls for each player
    round_rolls = []
    for player in players:
        roll1 = rollD6()
        roll2 = rollD8()
        total = roll1 + roll2
        player["rolls"].append(total)
        round_rolls.append(total)
        print(f"{player['name']} rolled {roll1} (d6) + {roll2} (d8) = {total}")

    # Determine round winner(s)
    highest_score = max(round_rolls)
    winners = [p for p in players if p["rolls"][-1] == highest_score]

    if len(winners) == 1:
        winners[0]["wins"] += 1
        print(f"🏆 {winners[0]['name']} wins this round!")
    else:
        tied_names = ", ".join(p["name"] for p in winners)
        print(f"🤝 It's a tie between: {tied_names}. No points this round.")

    # Print current scoreboard
    scoreboard = " | ".join([f"{p['name']}: {p['wins']} wins" for p in players])
    print("📊 Current Scoreboard:", scoreboard)

    # Check for overall winner
    for player in players:
        if player["wins"] >= WINNING_SCORE:
            print(f"\n🏆 {player['name']} is the champion of Battle of Dices with {player['wins']} wins!")
            print(f"🔥 The battle lasted {round_number} rounds!")
            game_over = True
            break

    round_number += 1

# Save results to file
filename = input("\nEnter filename to save results (e.g., results.txt): ")
with open(filename, "w") as file:
    file.write("Player Information:\n")
    for player in players:
        file.write(f"Name: {player['name']}, Email: {player['email']}, Country: {player['country']}, Wins: {player['wins']}, Rolls: {player['rolls']}\n")

    file.write("\nRound History:\n")
    for r in range(round_number - 1):
        rolls_str = "; ".join([f"{p['name']} rolled {p['rolls'][r]}" for p in players])
        file.write(f"Round {r+1}: {rolls_str}\n")

print(f"✅ Results saved to {filename}")
print("Game Over. Thanks for playing!")

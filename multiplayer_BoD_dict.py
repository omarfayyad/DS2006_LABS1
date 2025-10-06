import dice
import copy

# Variables to keep track of the score:
rounds = 0
gameover = False

# Number of wins needed to win the game:
winning_score = 3

#Dictionary template for storing player information
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": [],
}

#List to store the dicts for each player:
players = []

# Number of players:
num_of_players = int(input("Enter number of players: "))
# For loop to obtain player information:
for i in range(num_of_players):
    # Make a deep copy of the template for this player:
    player = copy.deepcopy(player_info)
    
    player ["name"] = input(f"Enter name for player {i+1}: ")
    player ["email"] = input(f"Enter email for player {i+1}: ")
    player ["country"] = input(f"Enter country for player {i+1}: ")
    players.append(player)
    
# Repeats until the game is over. As many rounds as needed:

while gameover is False:
    print(f"\n--- Round {rounds + 1} ---")
    input("\nPress Enter to roll the dice...")
    
    # dice roll for each player:
    current_rolls = []
    
    # We need to roll the dice for each player:
    for each_player in players:
        roll = dice.rollD6()
        
        #player_rolls_history[i].append(roll)
        each_player["rolls"].append(roll)
        current_rolls.append(roll)
        print(f"Player {each_player['name']} rolled a {roll}")
        
        
    # Determine the highest roll:
    max_roll = max(current_rolls)
    
    # find winners (there could be more than one):
    winners = []
    
    #Search for all players that got the max_roll:
    for each_player in players:
        if each_player["rolls"][-1] == max_roll:
           each_player["wins"] += 1
           print(f"Player {each_player['name']} wins this round!")
           winners.append(each_player["name"])
    print(f"Winners of this round: {winners}")
    
    # Check if any player has reached the winning score:
    for each_player in players:
        if each_player["wins"] >= winning_score:
            print(f"\nPlayer {each_player['name']} is the newest Battle of Dice champion!")
            gameover = True
    if gameover is False:
        print("No overall winner yet, the game continues, and DANGGG THIS BATTLE IS HEATED...")
    rounds += 1
    
# Save results to a file:
filename = input("Enter filename to save the results (e.g., results.txt): ")
with open(filename, 'w') as file:
   file.write("Player information: \n")
   
for each_player in players:
    file.write(f"Name: {each_player['name']}, Email: {each_player['email']}, Country: {each_player['country']}, Wins: {each_player['wins']}, Rolls: {each_player['rolls']}\n")
    
    file.write("\nGame Rounds: \n")
    
    #Round history:
    for r in range(rounds):
        # Start with empty text for this round:
        rolls_str = ""
       
       #Go through each player and build the string step by step
        for i, each_player in enumerate(players):
           rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}; "
           
            # Add a comma if not the last player:
        if i < len(players) - 1:
                rolls_str += ", "
                
        file.write(f"Round {r + 1}: {rolls_str}\n")
print(f"Results saved to {filename}")
print("Game Over. Thanks for playing!")

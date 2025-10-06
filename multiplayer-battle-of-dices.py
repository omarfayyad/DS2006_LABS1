import dice
import random 
gameover = False
winning_score = 3 # Numer of wins needed to win the game:
player_names = [] #Array to store the players' names:
player_wins = []  # Array for storing the number of wins for each player:
rounds= 0 #Number of rounds played
current_rolls = [] #Array to store the current rolls of each player in a round:

print("Welcome to the Multiplayer version of Battle of Dices!")
#Obtain number of players:
number_of_players = int(input("Please Enter number of players: "))
#For loop to obtain the player names:
for i in range(number_of_players):
    name = input(f"Enter name for player {i + 1}: ")
    player_names.append(name)
    
# initialize scores and rolls
for i in range(number_of_players):
    player_wins.append(0)
    
#Initialize player rolls as empty lists for each player
player_rolls_history = []
for i in range(number_of_players):
    # ADD an empty list for each player:
    player_rolls_history.append([])
    
#Game loop / repeat until the game is over

while gameover is False:
    rounds += 1
    print(f"Round {rounds}")
    # Dice rolls for each player in this round:
    player_rolls = []
    
    #Roll dice for each player:
    for i in range(number_of_players):
        roll = dice.rollD6()
        player_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"{player_names[i]} rolled a {roll}")
    
    highest_roll = max(player_rolls)
    winners = [i for i, r in enumerate(player_rolls) if r == highest_roll]
    
    if len(winners) == 1:
        winner_index = winners[0]
        player_wins[winner_index] += 1
        print(f"{player_names[winner_index]} wins this round!")
        
        if player_wins[winner_index] >= winning_score:
            print(f"{player_names[winner_index]} wins the game with {player_wins[winner_index]} wins!")
            gameover = True
            
    else:
        print("It's a tie between: " + ", ".join([player_names[i] for i in winners]))
        print("No points awarded this round.")
    
    #Check if someone reached the winning score:
    for i in range(number_of_players):
        if player_wins[i] >= winning_score:
            print(f"{player_names[i]} wins the game with {player_wins[i]} wins!")
            gameover = True   
        
    input("\nPress Enter to continue...")
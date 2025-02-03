import random
import math


#def roll():
   # min_val = 1;
    #max_val = 6;
    #roll = random.randint(min_val, max_val)

    #return roll

#value = roll()
#print(value)

while True:
    players = input("Enter number of players: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number of players must be between 2 and 4")
    else:
        print("Number of players must be a digit")

print("This is the correct number of players:", players)

max_score = 50
player_scores = [0 for _ in range(players)]
print(player_scores)


while max(player_scores) < max_score:
    
    for palyer_idx in range(players): # player_idx is the index of the player
        print("Player", palyer_idx + 1, "'s turn")
        current_score = 0

        while True:
            should_roll = input("Do you want to roll? (y)?: ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("you rolled a 1! Turn done!")
                current_score = 0
                break
            else:    
                current_score += value
                print("You rolled a", value)
            
            print("Your total score is:", current_score)

        player_scores[palyer_idx] += current_score
        print("Player", palyer_idx + 1, "scored", current_score, "points. Total:", player_scores[palyer_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player", winning_idx + 1, "wins with a score of", max_score)

#new change
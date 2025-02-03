import random
import math


def roll():
    min_val = 1;
    max_val = 6;
    roll = random.randint(min_val, max_val)

    return roll

value = roll()
print(value)

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
    

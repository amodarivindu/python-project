import random
import math


def roll():
    min_val = 1;
    max_val = 6;
    roll = random.randint(min_val, max_val)

    return roll

value = roll()
print(value)
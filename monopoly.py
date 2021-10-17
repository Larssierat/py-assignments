import random


#def throw_two_dice():

#def simulate_monopoly_games(total_games):

def throw_two_dice():
    dice = random.randint(1, 6)
    dice2= random.randint(1,6)
    total_throw= dice+dice2
    return total_throw

def simulate_monopoly():
    throw= 0
    position = 0
    while position <= 39:
        position= position+ throw_two_dice()
        throw = throw +1
        print (f"After throw {throw}: position {position}")

simulate_monopoly()
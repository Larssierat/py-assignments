import random


#def throw_two_dice():

#def simulate_monopoly_games(total_games):

board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                0, 320, 200, 0, 350, 0, 400]

possessions =  [0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0]

def throw_two_dice():
    dice = random.randint(1, 6)
    dice2= random.randint(1,6)
    total_throw= dice+dice2
    return total_throw




def simulate_monopoly():
    position = 0
    for throw in range(1,11):
        new_throw = throw_two_dice()
        if position+ new_throw<=39:
            position= position +new_throw
        else:
            position = ((position+new_throw)%39)-1

        if board_values[position]==0:
            value = 'empty'
        else:
            value = 'street'

        if value== 'street' and possessions[position]== 0:
            possessions[position]=1
        print (f"After throw {throw}: position {position} ({value})")
    print (possessions)



simulate_monopoly()

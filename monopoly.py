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

def throw_two_dice():           #function for throwing the dices
    dice = random.randint(1, 6)
    dice2= random.randint(1,6)
    total_throw= dice+dice2
    return total_throw

def simulate_monopoly():
    position = 0
    count_properties= 0
    count_throw= 0
    fields_for_sale= 28
    while fields_for_sale>0:    #throw
        new_throw = throw_two_dice()
        count_throw= count_throw+1
        if position+ new_throw<=39:      #determing position
            position= position +new_throw
        else:
            position = ((position+new_throw)%39)-1

        if board_values[position]==0:     #determing board value
            value = 'empty'
        else:
            value = 'street'
        #print (f"After throw {count_throw}: position {position} ({value})")

        if value== 'street' and possessions[position]== 0:
            possessions[position]=1
            count_properties= count_properties+1
            fields_for_sale= fields_for_sale - 1
            #print (f"player 1 has {count_properties} property in their possession there are still {fields_for_sale} fields for sale")
    return (count_throw)

number_of_throws = simulate_monopoly()
print(f"Done! After throw {number_of_throws} the player owned all properties.")



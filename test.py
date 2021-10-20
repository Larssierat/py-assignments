import random
import numpy as np
import matplotlib.pyplot as plt

def throw_two_dice():           #function for throwing the dices
    dice = random.randint(1, 6)
    dice2= random.randint(1,6)
    total_throw= dice+dice2
    return total_throw

def simulate_monopoly(starting_money_p1,starting_money_p2):
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                    0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                    0, 320, 200, 0, 350, 0, 400]

    possessions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    position_p1 = 0
    position_p2=0
    count_properties_p1= 0
    count_properties_p2=0
    fields_for_sale= 28
    start = 200
    while fields_for_sale>0:    #throw
        first_throw = throw_two_dice()
        second_throw= throw_two_dice()
        if position_p1+ first_throw<=39:      #determing position
            position_p1= position_p1 +first_throw
        else:
            position_p1 = ((position_p1+first_throw)%39)-1
            starting_money_p1= starting_money_p1+start

        if board_values[position_p1]==0:     #determining board value
            value = 'empty'
        else:
            value = 'street'


        if value== 'street' and possessions[position_p1]== 0 and board_values[position_p1]<=starting_money_p1:
            possessions[position_p1]=1
            count_properties_p1= count_properties_p1+1
            fields_for_sale= fields_for_sale - 1
            starting_money_p1= starting_money_p1-board_values[position_p1]


        if position_p2+ second_throw<=39:      #determing position
            position_p2= position_p2 +second_throw
        else:
            position_p2 = ((position_p2+second_throw)%39)-1
            starting_money_p2= starting_money_p2+start

        if board_values[position_p2]==0:     #determining board value
            value = 'empty'
        else:
            value = 'street'


        if value== 'street' and possessions[position_p2]== 0 and board_values[position_p2]<=starting_money_p2:
            possessions[position_p2]=1
            count_properties_p2= count_properties_p2+1
            fields_for_sale= fields_for_sale - 1
            starting_money_p2= starting_money_p2-board_values[position_p2]
    delta = count_properties_p1-count_properties_p2


    return (delta)

#print (simulate_monopoly(1500, 1500))
def simulate_monopoly_games(total_games,starting_money_p1,starting_money_p2):
    list_games=[]
    sum_difference_properties= 0
    for game in range(0,total_games):
        difference_properties= simulate_monopoly(starting_money_p1,starting_money_p2)
        list_games.append(difference_properties)
        sum_difference_properties=sum_difference_properties+difference_properties
    average_difference_properties= sum_difference_properties/total_games
    return average_difference_properties
total_games= 2500
starting_money_p1= 1500
starting_money_p2= 1500
print(simulate_monopoly_games(2500, 1500, 1500))

#x_values= []
#y_values=[]
#for i in range(0,3500,500):
#    x_values.append(i)
#    y_values.append(simulate_monopoly_games(total_games,i))
#plt.plot(x_values,y_values, 'b-')
#plt.xlabel("starting money")
#plt.ylabel("average number of throws")
#plt.show()

#print (f"Monopoly simulator: 1 player, Trump mode We simulated {total_games} games It took an average of {simulate_monopoly_games(total_games, starting_money_p1)} throws for the player to collect all streets")





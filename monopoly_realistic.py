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
    positions = [0,0]
    count_properties_p1= 0
    count_properties_p2=0
    fields_for_sale= 28
    start = 200
    while fields_for_sale>0:    #throw
        first_throw = throw_two_dice()
        second_throw= throw_two_dice()
        if positions[0]+ first_throw<=39:      #determing position
            positions[0]= positions[0] +first_throw
        else:
            positions[0] = ((positions[0]+first_throw)%39)-1
            starting_money_p1= starting_money_p1+start

        if board_values[positions[0]]==0:     #determining board value
            value = 'empty'
        else:
            value = 'street'


        if value== 'street' and possessions[positions[0]]== 0 and board_values[positions[0]]<=starting_money_p1:
            possessions[positions[0]]=1
            count_properties_p1= count_properties_p1+1
            fields_for_sale= fields_for_sale - 1
            starting_money_p1= starting_money_p1-board_values[positions[0]]


        if positions[1]+ second_throw<=39:      #determing position
            positions[1]= positions[1] +second_throw
        else:
            positions[1] = ((positions[1]+second_throw)%39)-1
            starting_money_p2= starting_money_p2+start

        if board_values[positions[1]]==0:     #determining board value
            value = 'empty'
        else:
            value = 'street'


        if value== 'street' and possessions[positions[1]]== 0 and board_values[positions[1]]<=starting_money_p2:
            possessions[positions[1]]=1
            count_properties_p2= count_properties_p2+1
            fields_for_sale= fields_for_sale - 1
            starting_money_p2= starting_money_p2-board_values[positions[1]]
    delta = count_properties_p1-count_properties_p2


    return (delta)

def simulate_monopoly_games(total_games,starting_money_p1,starting_money_p2):
    list_games=[]
    sum_difference_properties= 0
    for game in range(0,total_games):
        difference_properties= simulate_monopoly(starting_money_p1,starting_money_p2)
        list_games.append(difference_properties)
        sum_difference_properties=sum_difference_properties+difference_properties
    average_difference_properties= sum_difference_properties/total_games
    return average_difference_properties
total_games= 10000
starting_money_p1= 1500

print (f"Monopoly simulator: two players, 1500 euro starting money, 10000 games on average player 1 has {round((simulate_monopoly_games(10000, 1500, 1500)), 2)} more streets in their possession when all streets have been bought")

def equilibrium():
    x_values = []
    y_values = []
    positive_y_values=[]
    negative_y_values=[]
    positive_x_values=[]
    negative_x_values=[]
    for extra in range(0,250,50):
        starting_money_p2= 1500+extra
        more_streets= simulate_monopoly_games(total_games,starting_money_p1,starting_money_p2)
        print (f"starting money{starting_money_p1, starting_money_p2}: player 1 on average {round((more_streets),2)} more streets (player 2 {extra} euros extra)")
        x_values.append(extra)
        y_values.append(more_streets)

        if more_streets>0:                         #calculation equilibrium
            positive_y_values.append(more_streets)
            positive_x_values.append(extra)
        elif  more_streets<0:
            negative_y_values.append(more_streets)
            negative_x_values.append(extra)

    linear_coefficient= (positive_y_values[-1]-negative_y_values[0])/50
    precise_euros= positive_y_values[-1]/linear_coefficient
    equilibrium_money= positive_x_values[-1]+precise_euros
    if 75<equilibrium_money<125:
        equilibrium_money=100
    elif 125<equilibrium_money<175:
        equilibrium_money=150
    print (f"Monopoly simulator: 2 players on average,if player 2 receives {equilibrium_money} euros more starting money, both players collect an equal number of streets")


    plt.plot(x_values,y_values, 'b-')
    plt.axhline(y=0, color= 'r', linestyle= '-')
    plt.xlabel("extra starting money")
    plt.ylabel("more streets")
    plt.show()


equilibrium()


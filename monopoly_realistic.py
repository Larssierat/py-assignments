# Name: Lars Sierat
# Date: 25-11-2021
# Description: This program simulates a game of monopoly between two players more realistically by including the advantage a player has by throwing first.

import random
import matplotlib.pyplot as plt


# throwing two dices and returning the sum of the two dices
def throw_two_dice():
    dice = random.randint(1, 6)
    dice2= random.randint(1,6)
    total_throw= dice+dice2
    return total_throw

# simulates a game of monopoly between 2 players and returns the difference in amount of properties
def simulate_monopoly(starting_money_p1,starting_money_p2):
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                    0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                    0, 320, 200, 0, 350, 0, 400]
    possessions = []
    for i in range (len(board_values)):
        possessions.append(0)

    # situation at the start of the game
    positions = [0,0]
    count_properties_p1= 0
    count_properties_p2=0
    fields_for_sale= 0
    for value in board_values:
        if value != 0:
            fields_for_sale = fields_for_sale+1
    start = 200

    while fields_for_sale>0:
        first_throw = throw_two_dice()
        second_throw= throw_two_dice()

        if positions[0]+ first_throw<=39:      # 39 is the amount of fields
            positions[0]= positions[0] +first_throw
        else:
            positions[0] = ((positions[0]+first_throw)%39)-1   # -1 because the starting position is on field 0
            starting_money_p1= starting_money_p1+start

        if board_values[positions[0]]==0:
            value = 'empty'
        else:
            value = 'street'

        if value== 'street' and possessions[positions[0]]== 0 and board_values[positions[0]]<=starting_money_p1:
            possessions[positions[0]]=1
            count_properties_p1= count_properties_p1+1
            fields_for_sale= fields_for_sale - 1
            starting_money_p1= starting_money_p1-board_values[positions[0]]

        if positions[1]+ second_throw<=39:
            positions[1]= positions[1] +second_throw
        else:
            positions[1] = ((positions[1]+second_throw)%39)-1
            starting_money_p2= starting_money_p2+start

        if board_values[positions[1]]==0:
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

# simulates a certain amount of games and returns the average difference in properties between the two players
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

# calculates and plots at which amount of starting money for player 2 none of the players have an advantage in the game
def equilibrium():
    x_values = []
    y_values = []
    positive_y_values=[]
    negative_y_values=[]
    positive_x_values=[]
    negative_x_values=[]

    # calculates the effect of extra starting money on the difference in properties
    for extra in range(0,250,50):
        starting_money_p2= 1500+extra
        more_streets= simulate_monopoly_games(total_games,starting_money_p1,starting_money_p2)
        print (f"starting money{starting_money_p1, starting_money_p2}: player 1 on average {round((more_streets),2)} more streets (player 2 {extra} euros extra)")
        x_values.append(extra)
        y_values.append(more_streets)
        if more_streets>0:
            positive_y_values.append(more_streets)
            positive_x_values.append(extra)
        elif  more_streets<0:
            negative_y_values.append(more_streets)
            negative_x_values.append(extra)

    # calculates the equilibrium
    linear_coefficient= (positive_y_values[-1]-negative_y_values[0])/50
    precise_euros= positive_y_values[-1]/linear_coefficient
    equilibrium_money= positive_x_values[-1]+precise_euros
    if 75<equilibrium_money<125:
        equilibrium_money=100
    elif 125<equilibrium_money<175:
        equilibrium_money=150
    print (f"Monopoly simulator: 2 players on average,if player 2 receives {equilibrium_money} euros more starting money, both players collect an equal number of streets")

    # plots the effect of extra starting money on the difference in streets
    plt.plot(x_values,y_values, 'b-', label="more streets player 1")
    plt.axhline(y=0, color= 'r', linestyle= '-', label= "no difference")
    plt.xlabel("extra starting money player 2")
    plt.ylabel("more streets")
    plt.title ("correlation: extra starting money, the difference between the players")
    plt.legend(loc="upper right")
    plt.show()


equilibrium()


# Name: Lars Sierat
# Date: 25-11-2021
# Description: This program simulates a great number of games of a simplified version of the game Monopoly.


import random
import matplotlib.pyplot as plt

# throwing two dices and returns the sum
def throw_two_dice():
    dice = random.randint(1, 6)
    dice2= random.randint(1,6)
    total_throw= dice+dice2
    return total_throw

# simulates one game of monopoly and returns the amount of throws for the game to finish
def simulate_monopoly(starting_money):
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                    0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                    0, 320, 200, 0, 350, 0, 400]
    possessions= []
    for i in range(len(board_values)):
        possessions.append(0)

    # situation when the game starts
    position = 0
    count_properties= 0
    count_throw= 0
    fields_for_sale= 0
    for value in board_values:
        if value != 0:
            fields_for_sale= fields_for_sale+1
    start = 200

    while fields_for_sale>0:
        new_throw = throw_two_dice()
        count_throw= count_throw+1
        if position+ new_throw<=39:     # 39 is the amount of fields
            position= position +new_throw
        else:
            position = ((position+new_throw)%39)-1   # -1 because first field is position 0
            starting_money= starting_money+start

        if board_values[position]==0:
            value = 'empty'
        else:
            value = 'street'

        if value== 'street' and possessions[position]== 0 and board_values[position]<=starting_money:
            possessions[position]=1
            count_properties= count_properties+1
            fields_for_sale= fields_for_sale - 1
            starting_money= starting_money-board_values[position]
    return (count_throw)

# returns the average number of throws for a certain amount of games played
def simulate_monopoly_games(total_games,starting_money):
    list_games=[]
    sum_of_throws= 0
    for game in range(0,total_games):
        number_of_throws= simulate_monopoly(starting_money)
        list_games.append(number_of_throws)
        sum_of_throws=sum_of_throws+number_of_throws
    average_number_of_throws= sum_of_throws/total_games
    return average_number_of_throws
total_games= 2500
starting_money= 0

# graph that shows the effect of different amounts of starting money on the average number of throws
x_values= []
y_values=[]
for i in range(0,3500,500):
    x_values.append(i)
    y_values.append(simulate_monopoly_games(total_games,i))
plt.plot(x_values,y_values, 'b-')
plt.xlabel("starting money")
plt.ylabel("average number of throws")
plt.title("correlation between number of throws and starting money")
plt.show()

print (f"Monopoly simulator: 1 player, Trump mode We simulated {total_games} games It took an average of {simulate_monopoly_games(total_games, starting_money)} throws for the player to collect all streets")



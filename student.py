# Name: Lars Sierat
# Date: 25-11-2021
# Description: This program simulates the behavior of two drunk students in a graph.

import math
import random
import matplotlib.pyplot as plt

dotsY= []
dotsX= []
dotsY2= []
dotsX2= []

# range of axis
dimensionsX = [-20, 20]
dimensionsY = [-20, 20]

# determine starting point of students
previousY= 0
previousX=0
previousY2=0
previousX2=0

Distance= 1
markersize= 5

# creating a list with all possible angles
angle_list =[]
for i in range(0, 360):
    angle_list.append(i)

# count steps
count= 0

# formula creating the drunk step
for j in range(200):
    newY = previousY +(Distance * math.sin(random.choice(angle_list)))
    newX = previousX+(Distance * math.cos(random.choice(angle_list)))
    previousY= newY
    previousX= newX
    newY2= previousY2+ (Distance * math.sin(random.choice(angle_list)))
    newX2= previousX2+ (Distance * math.cos(random.choice(angle_list)))
    previousY2= newY2
    previousX2= newX2
    dotsY.append(newY)
    dotsX.append(newX)
    dotsY2.append(newY2)
    dotsX2.append(newX2)
    count = count +1

    point= [newX, newY]
    point2= [newX2, newY2]
    x_values= [point[0], point2[0]]
    y_values= [point[1], point2[1]]

    # plot the route of the first student
    plt.plot(dotsX, dotsY, 'b-')

    # location of the first student
    plt.plot(newX, newY, 'bo', markersize)

    # route of the second student
    plt.plot(dotsX2, dotsY2, 'g-')

    # location of the second student
    plt.plot(newX2, newY2, 'go', markersize)

    # connects the location of the first and second student
    plt.plot(x_values, y_values, 'r-')

    # shows the amount of steps taken
    plt.text(-17.5, -17.5,"(step %.0f/200)" %(count))

    # plot the axis
    plt.xlim(dimensionsX[0], dimensionsX[1])
    plt.ylim(dimensionsY[0], dimensionsY[1])

    # update graph
    plt.draw()
    plt.pause(0.001)

    #clear graph
    plt.clf()



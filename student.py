import math
import random

import numpy as np
import matplotlib.pyplot as plt

dotsY= []
dotsX= []
dotsY2=[]
dotsX2=[]
dimensionsX = [-20, 20]
dimensionsY = [-20, 20]
previousY= 0
previousX=0
previousY2=0
previousX2=0
Distance= 1
markersize= 5
angle_list =[]
for i in range(0, 360):
    angle_list.append(i)
count= 0

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

    plt.plot(dotsX, dotsY, 'b-') # first line
    plt.plot(newX, newY, 'bo', markersize)

    plt.plot(dotsX2, dotsY2, 'g-') # second line
    plt.plot(newX2, newY2, 'go', markersize)

    plt.plot(x_values, y_values, 'b-')

    plt.text(-17.5, -17.5,"(step %.0f/200)" %(count))


    plt.xlim(dimensionsX[0], dimensionsX[1])
    plt.ylim(dimensionsY[0], dimensionsY[1])

    # update graph
    plt.draw()
    plt.pause(0.001)

    #clear graph
    plt.clf()



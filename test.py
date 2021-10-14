import math
import random

import numpy as np
import matplotlib.pyplot as plt

dotsY= []
dotsX= []
dotsY2=[]
dotsX2=[]
dimensionsX = [-2, 2]
dimensionsY = [-2, 2]
Distance= 2
markersize= 5
angle_list =[]
for i in range(0, 360):
    angle_list.append(i)

for j in range(200):
    newY = Distance * math.sin(random.choice(angle_list))
    newX = Distance * math.cos(random.choice(angle_list))
    newY2= Distance * math.sin(random.choice(angle_list))
    newX2= Distance * math.cos(random.choice(angle_list))
    dotsY.append(newY)
    dotsX.append(newX)
    dotsY2.append(newY2)
    dotsX2.append(newX2)

    #plt.plot(dotsX, dotsY, 'b-')
    #plt.plot(newX, newY, 'bo', markersize) # blue dot

    plt.plot(dotsX2, dotsY2, 'r-')
    plt.plot(newX2, newY2, 'ro', markersize)


    plt.xlim(dimensionsX[0], dimensionsX[1])
    plt.ylim(dimensionsY[0], dimensionsY[1])

    # update graph
    plt.draw()
    plt.pause(1)

    #clear graph
    plt.clf()

# 1 punt in het centrum
# random een kant op met 1
previous_y
previous_x

import math
import numpy as np
import matplotlib.pyplot as plt

dotsY= []
dotsX= []
dimensionsX = [-10, 10]
dimensionsY = [-10, 10]
originDistance= 10
markersize= 5

#take small steps in x
for iteration in np.arange(0, 20, 0.1):
    radian = iteration
    newDistance= originDistance - (radian*0.5)
    newY = newDistance * math.sin(radian)
    newX = newDistance * math.cos(radian)

    dotsY.append(newY)
    dotsX.append(newX)

    plt.plot(dotsX, dotsY, 'bo', markersize) # blue dot

    plt.xlim(dimensionsX[0], dimensionsX[1])
    plt.ylim(dimensionsY[0], dimensionsY[1])

    # update graph
    plt.draw()
    plt.pause(0.001)

    #clear graph
    plt.clf()

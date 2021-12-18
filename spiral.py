# Name: Lars Sierat
# Date: 25-11-2021
# # Description: This program animates a spiraling dot.
# # The dot spins with a specific angular velocity around and with each step in time not only changes angle, but also decreases its radius until it eventually arrives exactly in the center.

import math
import numpy as np
import matplotlib.pyplot as plt

dotsY= []
dotsX= []

# range of axis
dimensionsX = [-10, 10]
dimensionsY = [-10, 10]

originDistance= 10
markersize= 5

# formula to determine new Y dot and new X dot
for iteration in np.arange(0, 20, 0.1):
    radian = iteration
    newDistance= originDistance - (radian*0.5)
    newY = newDistance * math.sin(radian)
    newX = newDistance * math.cos(radian)

    dotsY.append(newY)
    dotsX.append(newX)

    plt.plot(dotsX, dotsY, 'bo', markersize)

    plt.xlim(dimensionsX[0], dimensionsX[1])
    plt.ylim(dimensionsY[0], dimensionsY[1])

    # update graph each time new dots are added
    plt.draw()
    plt.pause(0.001)

    #clear graph
    plt.clf()

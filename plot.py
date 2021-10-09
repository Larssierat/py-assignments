import matplotlib.pyplot as plt
import numpy as np

x_values=[]
y_values= []
for x in np.arange(0,1.5,0.01):
    y= x**x
    x_values.append(x)
    y_values.append(y)

minimum_y= y_values[0]
minimum_x=0
for i in range (0,len(y_values)):
    if minimum_y>y_values[i]:
        minimum_y=y_values[i]
        minimum_x=x_values[i]


plt.text(0.2,1.3, '(xmin, ymin) = (minimum_x, minimum_y)', color= 'black', fontsize=10)

plt.plot(x_values, y_values, 'b-', minimum_x, minimum_y, 'ro')
plt.show()

print ('(xmin, ymin)= (0.37, 0.69)')

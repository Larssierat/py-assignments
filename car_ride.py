import matplotlib.pyplot as plt

input_file = open('CarRideData.csv', 'r')
x_values_time= []
y_values_speed= []
latitude= []
longitude= []
for line in input_file:
    split_data = line.split(',')
    x_values_time.append(split_data[1])
    y_values_speed.append(split_data[6])
    latitude.append(split_data[3])
    longitude.append((split_data[4]))
x_values_time.pop(0)
y_values_speed.pop(0)
latitude.pop(0)
longitude.pop(0)
traveled_distance= 0
for i in range(0,len(y_values_speed)):
    y_values_speed[i]= (float((y_values_speed[i]))*3.6)   #speed to km/h
    traveled_distance= traveled_distance+ (y_values_speed[i]/3600)
    x_values_time[i]= int(x_values_time[i])
    latitude[i]= float(latitude[i])
    longitude[i]= float(longitude[i])
traveled_distance= round(traveled_distance, 3)
print (f"The estimated travelled distance is {traveled_distance} km")

# graph speed/time
plt.figure(figsize=(20, 8))     #resize
plt.ylabel("speed km/h")
plt.xlabel("time in seconds(date 19-11-2014)")
plt.plot(x_values_time, y_values_speed, '-')
plt.margins(0.01)
plt.title('speed at a certain time')
plt.show()


color=[]
for i in range (0, len(y_values_speed)):
    if y_values_speed[i]>50:
        color.append('g')
    else:
        color.append('r')

plt.figure(figsize=(20, 8))
plt.ylabel("latitude")
plt.xlabel("longitude")
plt.scatter(longitude,latitude,s=5,color=color)
plt.margins(0.01)

plt.show()


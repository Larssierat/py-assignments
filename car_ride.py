import matplotlib.pyplot as plt


input_file = open('CarRideData.csv', 'r')
x_values_time= []
y_values_speed= []
latitude= []
longitude= []
for line in input_file:
    split_data = line.split(',')
    x_values_time.append(split_data[0][11:])
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
traveled_distance= round(traveled_distance, 3)
print (f"The estimated travelled distance is {traveled_distance}")

# graph speed/time
plt.figure(figsize=(20, 5))     #resize

plt.ylabel("speed km/h")        #labels
plt.xlabel("time(date 19-11-2014")
plt.plot(x_values_time, y_values_speed, '-')
plt.xticks(x_values_time[::10], rotation='vertical', fontsize= '6')
plt.margins(0.1)
plt.show()


latitude_above_50=[]
longitude_above_50= []
latitude_under_50= []
longitude_under_50= []
for i in range (0, len(y_values_speed)):
    if y_values_speed[i]>50:
        latitude_above_50.append(latitude[i])
        longitude_above_50.append(longitude[i])
    else:
        latitude_under_50.append(latitude[i])
        longitude_under_50.append(longitude[i])

plt.figure(figsize=(40, 5))     #resize

plt.ylabel("longitude")        #labels
plt.xlabel("latitude")
plt.plot(latitude, longitude, '-')
plt.xticks(x_values_time[::10], rotation='vertical', fontsize= '6')
plt.margins(0.1)



plt.axis([ 4.8, 5, 52.3, 52.4])


plt.show()





input_file.close()
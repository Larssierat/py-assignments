# Name: Lars Sierat
# Date: 25-11-2021
# Description: This file reads two datafiles containing the daily maximum and minimum temperature from 01-01-1901 till 31-07-2015 and returns information about this data

import datetime
import matplotlib.pyplot as plt


# reads data
input_file_max= open('DeBiltTempMaxOLD.txt', 'r')
input_file_min= open('DeBiltTempMinOLD.txt', 'r')

# extracts the dates and the temperatures of the data files
def read_data(file):
    dates= []
    temps= []
    for line in file:
        split_data= line.split(',')
        if split_data[0] == '   162':
            split_data[3]= int(split_data[3])
            dates.append(split_data[2])
            temps.append(split_data[3])
    return (dates, temps)

max_dates, max_temps= read_data(input_file_max)
min_dates, min_temps= read_data(input_file_min)

# confers date to integer and correct sequence
def date(temp_date):
    day= int(temp_date[6:8])
    month= int(temp_date[4:6])
    year= int(temp_date[0:4])
    x= datetime.datetime(year, month, day)
    return x.strftime("%d %b %Y")

# returns the highest temperature and the date of that temperature
def get_highest_temp(input_dates, input_temps):
    highest_temp= 0
    highest_temp_date=0
    for i in range(len(input_temps)):
        input_temps[i]= int(input_temps[i])
        if input_temps[i]>highest_temp:
            highest_temp= (input_temps[i])
            highest_temp_date= date(input_dates[i])
    return highest_temp_date, highest_temp

# returns the lowest temperature and the date of that temperature
def get_lowest_temp(input_dates, input_temps):
    lowest_temp= 0
    lowest_temp_date= 0
    for i in range(len(input_temps)):
        input_temps[i]= int(input_temps[i])
        if input_temps[i]<lowest_temp:
            lowest_temp= (input_temps[i])
            lowest_temp_date= date(input_dates[i])
    return lowest_temp_date, lowest_temp

highest_temp_date, highest_temp = get_highest_temp(max_dates, max_temps)
lowest_temp_date, lowest_temp = get_lowest_temp(min_dates, min_temps)

# returns the longest period of freezing and the date the frost ended
def get_coldest_freezing():
    count = 0
    longest_freezing_list=[]
    end_date_list= []

    # determines all freezing periods and the date the frosts ended
    for i in range (len(max_temps)):
        if max_temps[i]<0:
            count = count+1
        elif max_temps[i]>=0 and max_temps[i-1]<0:
            longest_freezing_list.append(count)
            end_date_list.append(max_dates[i-1])
            count = 0

    # determines which freezing period was the longest and which end date corresponded
    longest_freezing_period = 0
    end_date_freezing= 0
    for i in range (len(longest_freezing_list)):
        if longest_freezing_list[i]> longest_freezing_period:
            longest_freezing_period= longest_freezing_list[i]
            end_date_freezing= date(end_date_list[i])
    return longest_freezing_period, end_date_freezing

longest_freezing_period, end_date_freezing= (get_coldest_freezing())

# returns a graph with the number of the hot and tropical days for each year
def hot_days_graph():
    summer_days_count=0
    tropical_days_count=0

    # graph values
    summer_list=[]
    tropical_list=[]
    year_list=[]

    for i in range(len(max_temps)):

        # determining the year and counting the summer and tropical days
        if max_dates[i][0:4] == max_dates[i-1][0:4]:
            if max_temps[i]>=300:
                tropical_days_count= tropical_days_count+1
                summer_days_count= summer_days_count+1
            elif max_temps[i]>=250:
                summer_days_count= summer_days_count+1

        # switching to a new year and adding the tropical and summer days to the lists
        elif max_dates[i][0:4] != max_dates[i-1][0:4]:
            year_list.append(max_dates[i][0:4])
            summer_list.append(summer_days_count)
            tropical_list.append(tropical_days_count)
            summer_days_count=0
            tropical_days_count= 0

    # adding the summer and tropical days of the last year
    summer_list.append(summer_days_count)
    tropical_list.append(tropical_days_count)

    # removing the first wrong count of the first year
    summer_list.pop(0)
    tropical_list.pop(0)

    plt.figure(figsize=(20, 5))

    # plotting the summer days
    plt.bar(year_list, summer_list,color='b',label='summer days')

    # plotting the tropical days
    plt.bar(year_list, tropical_list,color='g',label='tropical days')

    plt.title('hot days per year')
    plt.xlabel('year')
    plt.ylabel('days')

    plt.xticks(rotation='vertical', fontsize='6')
    plt.yticks(rotation='horizontal', fontsize='10')
    plt.margins(0.001)
    plt.legend()
    return plt.show()


# returns the year in which the first heat wave occured
def get_first_heat_wave(max_dates, max_temps):
    temp_25= 0
    temp_30= 0

    # counting which year there are enough summer and tropical days
    for i in range (len(max_temps)):
        if max_temps[i]>=300:
            temp_30= temp_30+1
            temp_25= temp_25+1
        elif max_temps[i] >=250:
            temp_25=temp_25+1
        elif max_temps[i]<250:
            temp_25=0
            temp_30=0
        if temp_30>=3 and temp_25>=5:
            return max_dates[i][0:4]

year_heat_wave= get_first_heat_wave(max_dates, max_temps)

print (f"the highest temperature was {highest_temp/10} degrees and was measured on {highest_temp_date}")
print (f"the lowest temperature was {lowest_temp/10} degrees and was measured on {lowest_temp_date}")
print (f"The longest period of freezing had a duration of {longest_freezing_period} days and ended on {end_date_freezing}")
hot_days_graph()
print (f"The year in which the first heat wave occurred was {year_heat_wave}")
input_file_max.close()
input_file_min.close()










import datetime
import matplotlib.pyplot as plt
import numpy as np



input_file_max= open('DeBiltTempMaxOLD.txt', 'r')
input_file_min= open('DeBiltTempMinOLD.txt', 'r')

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



def date(temp_date):
    day= int(temp_date[6:8])
    month= int(temp_date[4:6])
    year= int(temp_date[0:4])
    x= datetime.datetime(year, month, day)
    return x.strftime("%d %b %Y")





def get_highest_temp(input_dates, input_temps):
    highest_temp= 0
    highest_temp_date=0
    for i in range(len(input_temps)):
        input_temps[i]= int(input_temps[i])
        if input_temps[i]>highest_temp:
            highest_temp= (input_temps[i])
            highest_temp_date= date(input_dates[i])
    return highest_temp_date, highest_temp

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


#print (f"the highest temperature was {highest_temp/10} degrees and was measured on {highest_temp_date}")
#print (f"the lowest temperature was {lowest_temp/10} degrees and was measured on {lowest_temp_date}")

def get_coldest_freezing():
    count = 0
    longest_freezing_list=[]
    end_date_list= []
    for i in range (len(max_temps)):
        if max_temps[i]<0:
            count = count+1
        elif max_temps[i]>=0 and max_temps[i-1]<0:
            longest_freezing_list.append(count)
            end_date_list.append(max_dates[i-1])
            count = 0
    longest_freezing_date = 0
    end_date_freezing= 0
    for i in range (len(longest_freezing_list)):
        if longest_freezing_list[i]> longest_freezing_date:
            longest_freezing_date= longest_freezing_list[i]
            end_date_freezing= date(end_date_list[i])
    return longest_freezing_date, end_date_freezing

longest_freezing_date, end_date_freezing= (get_coldest_freezing())
#print (f"The longest period of freezing had a duration of {longest_freezing_date} days and ended on {end_date_freezing}")

def hot_days_graph():
    summer_days_count=0
    tropical_days_count=0
    summer_list=[]
    tropical_list=[]
    year_list=[]
    for i in range(len(max_temps)):
        if max_dates[i][0:4] == max_dates[i-1][0:4]:
            if max_temps[i]>=300:
                tropical_days_count= tropical_days_count+1
                summer_days_count= summer_days_count+1
            elif max_temps[i]>=250:
                summer_days_count= summer_days_count+1
        elif max_dates[i][0:4] != max_dates[i-1][0:4]:
            year_list.append(max_dates[i][0:4])
            summer_list.append(summer_days_count)
            tropical_list.append(tropical_days_count)
            summer_days_count=0
            tropical_days_count= 0
    summer_list.append(summer_days_count)
    tropical_list.append(tropical_days_count)
    summer_list.pop(0)
    tropical_list.pop(0)

    plt.figure(figsize=(20, 5))
    plt.bar(year_list, summer_list,color='b',label='summer days')

    plt.bar(year_list, tropical_list,color='g',label='tropical days')

    plt.title('hot days per year')
    plt.xlabel('year')
    plt.ylabel('days')

    plt.xticks(rotation='vertical', fontsize='6')
    plt.yticks(rotation='horizontal', fontsize='10')
    plt.margins(0.001)
    plt.legend()
    return plt.show(), summer_list, tropical_list

print (hot_days_graph())
input_file_max.close()
input_file_min.close()








#def get_first_heat_wave(max_dates, max_temps):
#    temp_25=0
#    temp_30=0
#    for index,temp in enumerate(max_temps):
#        if temp_25 ==5 and temp_30==3:
#            return max_dates[index-1]
#        elif temp >=30:
#            temp_25 = temp_25+1
#            temp_30= temp_30+1
#        elif temp >=25:
#            temp_25= temp_25+1
#        elif temp <25:
#            temp_25=0
#            temp_30=0

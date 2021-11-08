import datetime
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


print (f"the highest temperature was {highest_temp/10} degrees and was measured on {highest_temp_date}")
print (f"the lowest temperature was {lowest_temp/10} degrees and was measured on {lowest_temp_date}")


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

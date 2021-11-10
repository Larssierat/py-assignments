ef tropical_summer_days():
    summer_days_count=0
    tropical_days_count=0
    summer_list=[]
    tropical_list=[]
    year_list=[]
    for i in range(len(max_temps)):
        if max_dates[i][0:4] == max_dates[i-1][0:4]:
            if max_temps[i]>=250:
                summer_days_count= summer_days_count+1
            elif max_temps[i]>=250 and max_temps[i]>=300:
                tropical_days_count=tropical_days_count+1
        elif max_dates[i][0:4] != max_dates[i-1][0:4]:
            year_list.append(max_dates[i][0:4])
            summer_list.append(summer_days_count)
            tropical_list.append(tropical_days_count)
            summer_days_count=0
            tropical_days_count= 0
    return year_list, summer_list, tropical_list

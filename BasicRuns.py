


import pandas as pnds

################## READING USING PANDAS INTO A DAT FRAME

crime_incidents = pnds.read_csv('Enter File Path Here', encoding='ISO-8859-1')
offense_dsc = pnds.read_csv('Enter File Path Here', encoding='ISO-8859-1')

############### RENAMING COLUMNS IN PYTHON ##############

print(crime_incidents.columns)
print(offense_dsc.columns)

offense_dsc = offense_dsc.rename(columns={"OLD COLUMN NAME":"NEW COLUMN NAME"})

print(crime_incidents.columns)
print(offense_dsc.columns)



########### CHECKING FOR DATA TYPES ################
print(type(crime_incidents))
print(type(offense_dsc))


########### Inner JOIN #######################

df_inner_join = pnds.merge(crime_incidents, offense_dsc, on = 'JOINED ON COLUMN NAME', how = "inner")

print(len(df_inner_join))

########### Left JOIN #######################

df_left_join = pnds.merge(offense_dsc, crime_incidents, on = 'JOINED ON COLUMN NAME', how = "left")

print(len(df_left_join))

########### Right JOIN #######################

df_right_join = pnds.merge(crime_incidents, offense_dsc, on = 'JOINED ON COLUMN NAME', how = "right")

print(len(df_right_join))

########### Full JOIN #######################

df_full_join = pnds.merge(crime_incidents, offense_dsc, on = 'JOINED ON COLUMN NAME', how = "outer")

print(len(df_full_join))


########### Cross JOIN ####################### - Doesnt work Ask Daniel about it

df_cross_join = pnds.merge(crime_incidents, offense_dsc, on = 'JOINED ON COLUMN NAME')

print(len(df_cross_join))


########### REMOVING COLUMNS FROM A DATA FRAME #######################

del df_inner_join['COLUMN NAME']

print(df_inner_join.columns)

########### ADDING COLUMNS TO A DATA FRAME #######################

df_inner_join['COLUMN NAME'] = crime_incidents['COLUMN NAME']


######### COUNTING INCIDENTS BY A FACTOR  ###########

incident_count = df_inner_join.groupby(['GROUP BY COLUMN NAME','GROUP BY COLUMN NAME']).count()['COLUMN TO BE ACCESSED']

print(incident_count)

################ READING USING CSV INTO A DICTIONARY
import csv

incidents_dict = []

with open('Enter your file path', 'r', newline='', encoding='ISO-8859-1') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        incidents_dict.append(row)
        ##print(len(row['INCIDENT_NUMBER']))

print(incidents_dict)

incidents_df = pnds.DataFrame(incidents_dict)


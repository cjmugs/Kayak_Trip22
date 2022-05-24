from tabulate import tabulate
# Data from GPS Garmin #
Elevation = 420
Elapse_Time = 6.29
Stopped_Time = 42.38
Trip_Odometer = 20.22
Max_Speed = 6.4
Moving_Average = (3.1 + 3.3 + 3.5) / 3
Overall_Average = (2.8 + 2.5 + 2.6) / 3

# Trip Info #
Launch_Site = "Boat Dock Road, Florence, IL"
End_Site = "Port of Grafton, Grafton, IL"

# Stops #
# 1) Campsite = Right acsending bank (Thursday Night / Friday Morning)
# 2) Kampsville = The Pavillion (To avoid the rain and get dry) (Friday Afternoon) - Robbie Left due to injury
# 3) Campsite = Big Fire to dry everything out (Friday Night / Saturday Morning)
# 4) Campsite = (Saturday Night / Sunday Morning)
# 5) Emergency Landing = Matt almost drowned due to shock from cut (Sunday Day)
# 6) Landed at Final Destination = Port of Grafton, Grafton, IL (Sunday Evening)

# Finished out the Illinois River this year #

# Crew #
table = [['First Name', 'Years on the Trip'], ['Chris', '11'], ['Matt', '11'], ['Steve', '8'],
         ['Scott', '8'], ['Ben', '6'], ['Robbie', '5']]

print(tabulate(table, headers='firstrow'))
print('\n')
print('Moving Average Speed ' + str(Moving_Average))
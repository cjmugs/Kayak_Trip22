from tabulate import tabulate
# Data from GPS Garmin #
Elevation = 420
Trip_Odometer = 55.22
Max_Speed = 6.4
Moving_Average = (3.1 + 3.3 + 3.8) / 3
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
def show_program():
    table = [['First Name', 'Last Name', 'Years on the Trip'], ['Chris', 'Mugavero', '11'], ['Matt', 'Shanks', '11'], ['Steve', 'Mugavero', '8'],
         ['Scott', 'Ustas', '8'], ['Ben', 'Chin', '6'], ['Robbie', 'Sliwinski', '5']]
    while True:
        print('\n')
        print(tabulate(table, headers='firstrow'))
        print('\n')
        print('Start From ' + Launch_Site)
        print('Ended in ' + End_Site)
        print('Moving Average Speed ' + str(Moving_Average))
        print('Max Speed ' + str(Max_Speed))
        print('Total Distance ' + str(Trip_Odometer))
        break
show_program()
# with open ("weather_data.csv") as data:
#      readable_data= data.readlines() 
#      print(readable_data)

# import csv
# with open ("weather_data.csv") as data:
#    w_data = csv.reader(data)
#    temperature = []
#    for row in w_data:
#        if row[1] != "temp":
#         temperature.append(int(row[1]))

# print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

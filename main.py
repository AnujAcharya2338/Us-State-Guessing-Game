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
# print(data)
# print(data["temp"])


# data_dict=data.to_dict()
# # print(data_dict)

# temp_list=data["temp"].to_list()
# avg = sum(temp_list) / len(temp_list)
# # print(avg)

# data["temp"].max()

# Get data in a row

# print(data[data.day == "Monday"])

# print(data[data.temp == data["temp"].max() ])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# faran=monday_temp *9/5 +32
# print(faran)

# Creating a dataframe from scratch

data_dict = {
    "dict":["Amy", "James", "Hanks"] ,
    "score":[89,54,97]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
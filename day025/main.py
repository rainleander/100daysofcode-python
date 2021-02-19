# with open("weather_data.csv") as weather:
#     data = [line.strip() for line in weather]
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list
# print(temp_list)
#
# # Challenge: find the temp avg for the week
# average_temp = data["temp"].mean()
# print(average_temp)
#
# # Challenge: find the highest temp for the week
# highest_temp = data["temp"].max()
# print(highest_temp)
#
# print(data["condition"])
# print(data.condition)

# # get a row of data
# print(data[data.day == "Monday"])

# # Challenge: get the day's info on the highest temp day
# print(data[data.temp == data.temp.max()])

# # Challenge: convert monday's temp to F
# monday = data[data.day == "Monday"]
# monday_f = (monday.temp * 1.8) + 32
# print(f"{monday_f} F")

# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

# Squirrel Challenge
# Create a CSV called squirrel_count.csv with Fur Color
# and Count based on the Primary Fur Color Column
# In 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
gray_fur = len(data[data["Primary Fur Color"] == "Gray"])
red_fur = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_fur, red_fur, black_fur],
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")

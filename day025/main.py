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

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
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

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")

# Using a built-in python package to parse data in csv files.
# import csv

# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []  # must be integers, not string
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# A more advanced package with analyzing tables.
import pandas

data = pandas.read_csv("weather_data.csv")
# temperatures = data["temp"].to_list()
# print(f"temperature list: {temperatures}")

# Calculating mean
# temp_avg = sum(temperatures)/len(temperatures)
# print(f"Avg  temp: {round(temp_avg, 2)}")
# print(f"Avg temp: {data['temp'].mean()}")
# print(f"Max temp: {data['temp'].max()}")

# Get data in columns:
# print(data['condition'])
# or
# print(data.condition)

# Get data from a specific row matching a value:
# Gets all occurrences
# print(data[data.condition == "Mostly Cloudy"])


# Challenge #1: Pull up the data where the temperature got it's maximum within the week.
# print(data[data.temp == data.temp.max()])


# Challenge #2: Convert monday's temperature to Celsius.
# def convert_fahrenheit_to_celsius(fahrenheit):
#     print(fahrenheit)
#     return float((fahrenheit - 32) * 5/9)
#
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp.iloc[0])
# monday_temp_C = convert_fahrenheit_to_celsius(monday_temp)
# print(f"Monday's fahrenheit temperature {monday_temp} in Celsius is: {round(monday_temp_C, 2)}")

# Creating dataframes:
grade_book = {
    "students": ["John", "Alex", "Eric", "James", "Gabriel"],
    "score": [68, 78, 100, 92, 95]
}
# Pass the dictionary to Dataframe constructor
data = pandas.DataFrame(grade_book)
# Printing our looks just like dataframe, it nicely formats it correctly!
print(data)

# Convert our dataframe into a csv file named "new_data.csv" in our project directory.
# It's not a perfect format. I don't like the first column. But it's a good start.
data.to_csv("new_data.csv")

import_data = pandas.read_csv("new_data.csv")
print(import_data)
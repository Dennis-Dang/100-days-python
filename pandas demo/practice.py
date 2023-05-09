import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Gray"])
cinnamon_squirrel_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Black"])

fur_color_data = {
    "fur color": ["gray", "cinnamon", "black"],
    "count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]

}

df = pandas.DataFrame(fur_color_data)
df.to_csv("squirrels_by_fur_color.csv")
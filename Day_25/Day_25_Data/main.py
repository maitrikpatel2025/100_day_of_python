# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     final_temp = temp[1:7]
#     print(final_temp)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel = len(data[data['Primary Fur Color'] == 'Gray'])
Cinnamon_squirrel = len(data[data['Primary Fur Color'] == 'Cinnamon'])
Black_squirrel = len(data[data['Primary Fur Color'] == 'Black'])
Red_squirrel = len(data[data['Primary Fur Color'] == 'red'])

print(gray_squirrel)
print(Cinnamon_squirrel)
print(Black_squirrel)
print(Red_squirrel)

data_dic = {
    "fur_color": ['Gray', "Cinnamon", "Black", "Red"],
    "count": [gray_squirrel, Cinnamon_squirrel, Black_squirrel, Red_squirrel]
}

df = pandas.DataFrame(data_dic)
df.to_csv("squrriel_count.csv")
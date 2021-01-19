
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 🚨 Do Not Change the code above 👆

#Exercise_1

#Write your 1 line code 👇 below:
multi_numbers = {num:num*num for num in numbers}
squared_numbers = {num: multi for (num, multi) in multi_numbers.items() if multi == num*4}

#Write your code 👆 above:
print(multi_numbers)
print(squared_numbers)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

import random


# Write your code below:
result = {name: len(name) for name in sentence.split()}

print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
weather_f = {day: (temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}

# Write your code 👇 below:



print(weather_f)

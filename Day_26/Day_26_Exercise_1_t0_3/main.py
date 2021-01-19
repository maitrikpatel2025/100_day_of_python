
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Exercise_1

#Write your 1 line code 👇 below:
squared_numbers = [num*num for num in numbers]

#Write your code 👆 above:
print(squared_numbers)

#Exercise_2

#Write your 1 line code 👇 below:
result = [num for num in numbers if num % 2 == 0 ]

#Write your code 👆 above:
print(result)

#Exercise_3

#Write your line code 👇 below:
with open("file1") as file1:
    data = file1.readlines()
    new_data_list = [num.split("\n")[0] for num in data]
    new_int_list = [int(num) for num in new_data_list ]


with open("file2") as file2:
    data2 = file2.readlines()
    new_data2_list = [num.split("\n")[0] for num in data2]
    new_int2_list = [int(num) for num in new_data2_list]

compare_list = [item for item in new_int_list if item in new_int2_list ]

print(compare_list)
#Write your line code 👇 below:
with open("file1") as file_1:
    data_1 = file_1.readlines()

with open("file2") as file_2:
    data_2 = file_2.readlines()

compare_list = [int(item) for item in data_1 if item in data_2]

print(compare_list)
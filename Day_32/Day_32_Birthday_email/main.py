import pandas
import datetime
import random
import smtplib

##################### Extra Hard Starting Project ######################
birth_data = {}


try:
    data = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("birthdays.csv")
    birth_data = original_data.to_dict(orient="records")
else:
    birth_data = data.to_dict(orient="records")

now = datetime.datetime.now()
month = now.month
day = now.day

birth_info = {}

for i in range(len(birth_data)):
    if birth_data[i]["month"] == month:
        if birth_data[i]["day"] == day:
            birth_info = birth_data[i]

print(birth_info)

name = birth_info["name"]
to_email = birth_info["email"]
my_email = "maitrik.patel3011@gmail.com"
password = "30112025"

file_name = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letter_tem = random.choice(file_name)

with open(f"letters/{letter_tem}", "r") as letter_templates_file:
    letter = str(letter_templates_file.read())
    new_letter = letter.replace("[NAME]", name)
    print(new_letter)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_email,
                        msg=f"Subject: Happy Birthday {name} \n\n {new_letter}")






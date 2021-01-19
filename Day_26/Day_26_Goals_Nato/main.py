# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_frame = pandas.DataFrame(data)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("Enter Name : ")
user_name_to_list  = [name.capitalize() for name in user_name]

# Method_1
# nato_name = {}
# for name in user_name_to_list:
#     for (index, nato) in data_frame.iterrows():
#         if nato.letter == name:
#            nato_name[name] = nato.code
# print(nato_name)

phonetic_code = {nato.letter : nato.code for (index, nato) in data_frame.iterrows()}
print(phonetic_code)

output_list = [phonetic_code[letter] for letter in user_name.upper()]
print(output_list)


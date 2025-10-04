student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass
    # print(key,value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
df = pandas.read_csv('nato_phonetic/nato_phonetic_alphabet.csv')
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index,row) in df.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

message = input().upper()
# message_list = [letter for letter in message]
phonetic_message = [phonetic_dict[letter] for letter in message]
print(phonetic_message)
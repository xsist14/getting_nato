student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
data_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
#Loop through rows of a data frame


nato_dict = {row.letter:row.code for (index, row) in data_dict.iterrows()}
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
response = input("input a word: ")
list_to_translate = [letter for letter in response]
translation = [nato_dict[letter.upper()] for letter in list_to_translate]
print(translation)

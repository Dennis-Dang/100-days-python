import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
    # Access key and value
    # print(key, value)


# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # print(row)
    # Access row.student or row.score
    # print(row.student)
    # print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

print(nato_dict)
# TODO: Create a list of the phonetic code words from a word that the user inputs.


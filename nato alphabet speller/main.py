import pandas

# Read csv file and data into a dictionary using dictionary comprehension.
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# nato_dict data representation looks like this:
# {
#   "A": "Alpha"
#   "B": "Bravo"
#   ....
#   "Z": "Zulu"

# Keep asking for user input until user enters "exit"
loop = True
while loop:
    word = input("Enter a word to turn into NATO: ")
    # Convert every letter into uppercase to later match with the keys of the NATO alphabet dictionary
    upper_word = [letter.upper() for letter in word]
    if upper_word != "EXIT":
        # Use the NATO dictionary to convert each letter into their corresponding NATO alphabet code.
        phonetic_word = [nato_dict[letter] for letter in upper_word if letter in nato_dict]
        print(phonetic_word)
    else:
        loop = False
        print("Goodbye!")

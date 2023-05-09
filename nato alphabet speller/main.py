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
    word = input("Enter a word to turn into NATO: ").upper()
    if word != "EXIT":
        # Use the NATO dictionary to convert each letter into their corresponding NATO alphabet code.
        # Condition in dictionary comprehension is necessary in case user enters a character outside of NATO alphabet.
        phonetic_word = [nato_dict[letter] for letter in word if letter in nato_dict]
        print(phonetic_word)
    else:
        loop = False
        print("Goodbye!")

import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

loop = True
while loop:
    word = input("Enter a word to turn into NATO: ")
    upper_word = [letter.upper() for letter in word]
    if upper_word != "EXIT":
        phonetic_word = [nato_dict[letter] for letter in upper_word if letter in nato_dict]
        print(phonetic_word)
    else:
        loop = False
        print("Goodbye!")

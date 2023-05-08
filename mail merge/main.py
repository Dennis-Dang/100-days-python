letter = ""
with open("./Input/Names/invited_names.txt") as file:
    invited = file.readlines()
    for i in range(0, len(invited)):
        invited[i] = invited[i].strip('\n')

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for name in invited:
    with open(f"./Output/ReadyToSend/{name.lower()}.txt", mode='w') as file:
        file.write(letter.replace("[name]", name))

names = []
with open("Input/Names/invited_names.txt") as data:
    names = [line.strip() for line in data]

starting_letter_list = []
with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    starting_letter_list = starting_letter.readlines()

new_address = []
for x in range(len(names)):
    new_address = starting_letter_list[0].replace("[name]", names[x])
    with open(f"Output/ReadyToSend/letter_to_{names[x]}.txt", mode="w") as file:
        file.write(f"{new_address}\n{starting_letter_list[2]}\n{starting_letter_list[4]}\n{starting_letter_list[6]}")

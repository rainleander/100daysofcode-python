import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

code_dict = {}
for (index, row) in data.iterrows():
    code_dict[row.letter] = row.code

# TODO: catch the keyerror when a user enters a character that is not in the dictionary
# TODO: provide feedback to the user when an illegal word is entered
# TODO: continue prompting the user to enter another word until they enter a valid word

user_input = input("Enter a word: ").upper()
list_of_code = [code_dict[letter] for letter in user_input]
print(list_of_code)

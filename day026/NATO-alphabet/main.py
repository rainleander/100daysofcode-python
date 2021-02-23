import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
code_dict = {}
for (index, row) in data.iterrows():
    code_dict[row.letter] = row.code

# Create a list of phonetic code words from a word the user inputs
user_input = input("Enter a word: ").upper()
list_of_code = [code_dict[letter] for letter in user_input]
print(list_of_code)

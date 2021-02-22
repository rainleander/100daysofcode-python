# List Comprehension
# Create a new list from a previous list
# new_list = [new_item for item in list]
numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Rain"
name_list = [letter for letter in name.lower()]
print(name_list)

# # Read the file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# # Read the file without using close()
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # Write to the file
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# # Append to the file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")
#

# Write to create a new file
with open("new_file.txt", mode="w") as file:
    file.write("New file text.")


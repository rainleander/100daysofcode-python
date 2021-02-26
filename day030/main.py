# --- Day 030 : Catching Exceptions --- #

'''
try: something that might cause an exception
except: do this if there WAS an exception
else: do this if there were NO exceptions
finally: do this no matter what happens
'''

# # FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'
# with open("a_file.txt") as file:
#     file.read()

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     # print("There was an error.") <-- kind of useless
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# # finally:
# #     file.close()
# #     print("File was closed.")
# finally:
#     raise TypeError("This is an error that I made up.")

# # KeyError: 'non_existent_key'
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# # IndexError: list index out of range
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# # TypeError: can only concatenate str (not "int") to str
# text = "abc"
# print(text + 5)

# raise: make your own error messages when the code is otherwise logical
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height is too high.")

bmi = weight / height ** 2
print(bmi)


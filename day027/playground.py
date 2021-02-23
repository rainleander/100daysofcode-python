# Challenge: modify the add function to take an unlimited number of arguments.
# Use a loop to sum all the arguments inside the function.
# Test it out by calling add() to calculate sum of some arguments

def add(*args):
    total = 0
    for x in args:
        total += x
    return total


numbers_list = (1, 2, 3, 45, 700)
print(add(numbers_list))

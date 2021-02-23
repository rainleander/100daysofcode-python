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


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(n, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.year = kw.get("year")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)

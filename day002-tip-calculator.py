# If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

tip /= 100 
tip += 1

# Each person should pay (150.00 / 5) * 1.12 = 33.6

per_person = (total_bill / people) * tip

# Format the result to 2 decimal places = 33.60 using %.2f

print("$%.2f" % per_person)

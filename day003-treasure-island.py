print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

left_or_right = input("You find yourself at a crossroads. Would you like to go left or right? ").lower()
if left_or_right == "left":
  swim_or_wait = input("You find yourself at a lake. Would you like to swim or wait? ").lower()
  if swim_or_wait == "wait":
    which_door = input("You are standing in front of three doors - a yellow one, a red one, and a blue one. Which door do you choose? ").lower()
    if which_door == "yellow":
      print("You have found the treasure! You win!")
    elif which_door == "red":
      print("Oh, no! You are burned by fire. Game over.")
    elif which_door == "blue":
      print("Oh, no! You are eaten by beasts. Game over.")
    else:
      print("Game over.")
  else:
    print("Oh, no! You are attacked by trout. Game over.")
else:
  print("Oh, no! You fall into a hole. Game Over.")

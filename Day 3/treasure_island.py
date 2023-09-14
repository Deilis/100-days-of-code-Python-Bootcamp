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
first_question = input("You're at a cross road. Where do you want to go? Type " '"left" or "right" ').lower()

if first_question == "left":
  second_question = input('You\'ve came to pond.\nThere\'s some kind a hatch in the middle of it.\nWhat will you do? Will you "wait" or will you "swim" there? ').lower()
  if second_question == "wait":
    third_question = input('You waited out, water went down.\nYou saw small bridge to island which was under water,\nYou passed bridge and opened hatch.\nYou went down and saw three door: "Red", "Blue", "Yellow". Which one will you choose? ').lower()
    if third_question == "red":
      print("You entered thru Red door.\nRoom closed behind you.\nFire started blazing.\n You burned by fire.\n GAME OVER")
    elif third_question == "blue":
      print("You entered thru Blue door.\nRoom closed behind you.\nYou heard noises and some one attacked you.\nIT WAS BEAST. You were eaten by beast.\nGAME OVER.")
    elif third_question == "yellow":
      print("You entered thru Yellow door.\nRoom did not close behind you. You found chest full of gold.\nCongratulation. YOU WON!")
    else: 
      print("You chose wrong. You died of hunger.\nGAME OVER.")
  elif second_question == "swim":
    print("You swam thru lake.\nHuge trout attacked you.\nGAME OVER.")
  else:
    print("You did nothing. You died of hunger.\nGAME OVER.")
else:
  print("You fell in to huge hole. There were a lot spikes. You died.\nGAME OVER.")

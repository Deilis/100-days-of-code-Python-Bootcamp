import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. Your choice: "))
random_choice = random.randint(0, 2)

print(f"Computer chose {random_choice}")

if user_input == 0 and random_choice == 2:
    print("You won vs Computer!")
elif random_choice == 0 and user_input == 2:
    print("Ahh.. you lost vs Computer!")
elif random_choice == user_input:
    print("It's a draw! ")
elif random_choice > user_input:
    print("Ahh.. you lost vs Computer!")
else:
    print("Wrong number, you lost.")

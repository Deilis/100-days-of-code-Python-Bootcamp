# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
people_eating = (len(names))

buying_food = random.randint(0, people_eating - 1)
buys_food = names[buying_food]

print(buys_food)


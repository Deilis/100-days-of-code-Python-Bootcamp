# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

string_combine = name1 + name2
lower = string_combine.lower()

t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")
score_one = t + r + u + e

l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")
score_two = l + o + v + e

final_score = int(str(score_one) + str(score_two))

if final_score < 10 or final_score > 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")

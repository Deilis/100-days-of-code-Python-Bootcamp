# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
death = 90 - age

days_in_year_rem = death * 365
weeks_in_year_rem = death * 52
months_in_year_rem = death * 12

death_sentence = f"You have {days_in_year_rem} days, {weeks_in_year_rem} weeks, and {months_in_year_rem} months left."
print(death_sentence)

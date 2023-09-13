print("How much should we pay?")

bill = float(input("Bill: "))
people = int(input("How many people ate? "))
tip = int(input("Tip amount? "))

payable_amount_tip = tip / 100 * bill + bill

total = payable_amount_tip / people
bill_to_pay = "{:.2f}".format(total)

print(f"Everyone should pay: ${bill_to_pay}.")

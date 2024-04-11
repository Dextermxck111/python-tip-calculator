print("Welcome to the Python Tip Calculator.")

total_bill = float(input("How much was the total bill? "))
percent_of_tip = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people will split the bill? "))

amount_after_tip = (total_bill / num_of_people) * (1 + (percent_of_tip / 100))
"{:.2f}".format(amount_after_tip)
print(f'Each person should pay: {"{:.2f}".format(amount_after_tip)}')
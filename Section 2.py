# Type
print("Number of letters in your name: " + str(len(input("Enter your name"))))

# Mathematical operations
print(3 * (3 + 3) / 3 - 3)

# Number Manipulation
bmi = int(84 / 1.65 ** 2)
print(bmi)

# Tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
tip_total = bill * tip_percent
bill_final = bill + tip_total
total_amount = round(bill_final / people, 2)
print(f"Each person should pay: ${total_amount}")

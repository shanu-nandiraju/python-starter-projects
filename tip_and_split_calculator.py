print("Welcome to the tip calculator!")

# Get and validate bill amount
bill = float(input("What was the total bill? $"))
while bill <= 0:
    print("Please enter a positive number for the bill.")
    bill = float(input("What was the total bill? $"))

# Get and validate tip percentage
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? : "))
while tip not in [10, 12, 15]:
    print("Please enter one of the following options: 10, 12, or 15.")
    tip = int(input("What percentage tip would you like to give? 10, 12, or 15? : "))

# Get and validate number of people
people = int(input("How many people to split the bill? : "))
while people <= 0:
    print("Please enter a number greater than zero for the number of people.")
    people = int(input("How many people to split the bill? : "))

# Calculate the tip percentage factor
percent = 1 + tip / 100

# Calculate the amount each person should pay
pay = (bill / people) * percent

# Print the result
print("Each person should pay: $" + str(round(pay, 2)))

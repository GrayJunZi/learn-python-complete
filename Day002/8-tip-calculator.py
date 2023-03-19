print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

pay =round( tip / 100 * bill + bill,2)
print(f"Each person should pay: ${pay}")

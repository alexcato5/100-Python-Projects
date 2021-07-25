# TIP CALCULATOR

total = float(input("What is the total amount to pay?\n\t>"))

tip_percentage = int(input("What percentage would you like to tip? (10, 12, 15)\n\t>"))

people = int(input("How many people are going to pay the bill?\n\t>"))

total_per_person = ( total + total*(tip_percentage/100) )/ people

print(f"Each person should pay ${total_per_person}")
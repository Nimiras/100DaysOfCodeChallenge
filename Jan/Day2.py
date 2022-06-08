
# Tip Calculator for Day 2 of the 100DaysOfCode Challenge
# Getting the correct numbers from the user via an input
price_bill = input("What was the total bill? ")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
number_of_people = input("How many people to split the bill?")

# calcualting the amount each person has to pay
bill_with_tip = float(price_bill)*((float(tip_percentage) / 100)+1)
bill_per_person = bill_with_tip / float(number_of_people)
print(f"Each person should pay: {format(bill_per_person, '.2f')}")

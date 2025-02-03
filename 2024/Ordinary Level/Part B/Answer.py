# Comment
# Examination number:

# Display Split Bill Calculator
print("Split Bill Calculator")

# Enter the total amount of the bill.
# This could be a decimal point so we will convert it to float
bill = float(input("How much is the bill?: "))

# Next we need to find out how many people this will be split between
# We are casting this to an int as their can't be half a person.
amountOfPeople = int(input("How many people?: "))

# We need to divide the bill between the amount of people. 
# This will give the amount owed by each
billPerPerson = bill / amountOfPeople

# We must now display the final bill per person
print("you each owe", billPerPerson)
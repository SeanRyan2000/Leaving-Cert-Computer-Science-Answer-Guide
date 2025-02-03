# Question 16(a)
# Examination Number:

# Modify the program so that it first prints out “Welcome to the driving licence eligibility
# checker” instead of “The program”. 

# We are going to change this print statement to the new line:
# "Welcome to the driving licence eligibility checker"

# print("The program")
print("Welcome to the driving licence eligibility checker")

age = int(input("What age are you? "))

if (age >= 17):
    print("You are entitled to apply for a driving licence.")
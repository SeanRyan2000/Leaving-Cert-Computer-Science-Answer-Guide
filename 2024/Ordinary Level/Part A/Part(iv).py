# Question 16(a)
# Examination Number:

#  Currently the program will only output a message when the entered age is 17 or over.
# Change the program so that if an age less than 17 is entered a suitable message is
# output. 

print("Welcome to the driving licence eligibility checker")

age = int(input("What age are you? "))
print("You entered ", age)

if (age >= 17):
    print("You are entitled to apply for a driving licence.")
# We will add an else statement. This will run if anything less than 17 is entered
else:
    print("You are not enitled to apply for a driving licenese")
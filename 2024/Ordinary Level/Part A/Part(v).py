# Question 16(a)
# Examination Number:

# Amend the program to ask for the user’s name. The name should be stored in an
# appropriate variable. The user’s name should be output along with the message about
# eligibility to apply for a licence. 

print("Welcome to the driving licence eligibility checker")

# Ask the user for their age. This is similar to the age input. 
# We do not need to set the type to int. As we would expect a string for a name.
name = input("What is your name?")

age = int(input("What age are you? "))
print("You entered ", age)

# We will also need to modify this to use the user's name
if (age >= 17):
    print(name, "You are entitled to apply for a driving licence.")
else:
    print(name, "You are not enitled to apply for a driving licenese")
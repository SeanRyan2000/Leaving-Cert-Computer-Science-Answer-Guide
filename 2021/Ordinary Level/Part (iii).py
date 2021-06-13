# Question 16(a)
# Examination Number:

# (iii) create a boolean variable loggedIn set to false
loggedIn = False

pin = "1579"

userTry = input("Enter PIN:") # (i) The input command is asking the user to type in their Pin code.

if userTry == pin:
    print("Welcome")
# (ii) add in else statement and print
else :
    print("Incorrect PIN")
# Question 16(a)
# Examination Number:

# Currently the user can enter a negative number. Negative numbers should not be
# allowed in this program. Amend the program so that the times table is not printed out
# and an appropriate error message is displayed if the user enters a negative number. 

print("********************")
print("Times Table program")
print("********************")

# We can do this by adding an if statement
number = int(input("Enter number: "))
# A negative number is any number less than 0
# if the number is less than 0 we will print that it cannot be input.
if (number < 0):
    print("This program does not support negative numbers")
# If the number is greater than 0 we should continue.
# We need to add this else statement and increment all code below by a "tab"
else:
    print("Multiplications of ", number)

    for i in range(10):
        print(number*i)
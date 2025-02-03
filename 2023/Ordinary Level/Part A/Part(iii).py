# Question 16(a)
# Examination Number:

# Amend the program to ask for and accept the user's choice of number to be used as
# the multiplier. Store the entered number in the variable called number.

print("********************")
print("Times Table program")
print("********************")

# We need to set up a user input.
# We can modify the number variable to accept input 
# instead of the hardcoded "7"

# We need to wrap this in the int method
# Otherwise it will read the number as a string
number = int(input("Enter number: "))

print("Multiplications of ", number)

for i in range(10):
    print(number*i)
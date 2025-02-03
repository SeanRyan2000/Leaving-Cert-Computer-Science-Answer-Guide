# Question 16(a)
# Examination Number:

# Times tables normally shows the result of multiplying a specific number by zero to
# twelve inclusive. Amend the program so it displays the results of multiplying the
# entered number by zero to twelve inclusive

print("********************")
print("Times Table program")
print("********************")


number = int(input("Enter number: "))
if (number < 0):
    print("This program does not support negative numbers")
else:
    print("Multiplications of ", number)

# We will need to change this for loop. Currently it is printing from 0-9.
# The range() function generates a sequence of numbers starting from 0 (by default) 
# up to but not including the given number (10).
    # for i in range(10):
    for i in range(13):
        print(number*i)
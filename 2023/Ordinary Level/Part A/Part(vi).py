# Question 16(a)
# Examination Number:

# Update the program so that it displays the results in the format “3 x 8 = 24”, as shown
# below. 

print("********************")
print("Times Table program")
print("********************")


number = int(input("Enter number: "))
if (number < 0):
    print("This program does not support negative numbers")
else:
    print("Multiplications of ", number)
    for i in range(13):
        # We need to edit the print statement so it will include the 
        # format "3*8" 
        # The value of "3" is equal to i. i is incrementing each time starting from 0
        # We are then multipling that value by the variable number the user has entered
        
        # print(number*i)
        print(i, "x", number, "=", number*i)

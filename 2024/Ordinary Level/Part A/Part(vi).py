# Question 16(a)
# Examination Number:

# Update your program so that it outputs a message to the user based on the criteria in
# the table below. The output should continue to display the user name. The name Sarah
# is used in the examples below. 
#       
#           Condition                       Output
# Age is less than 17                       Sarah you are not entitled to apply for a driving licence. 
# Age between 17 and 74 inclusive           Sarah you are entitled to apply for a driving license
# Age is more than 74                       Sarah you are entitled to apply for a three-year driving licence. 


print("Welcome to the driving licence eligibility checker")


name = input("What is your name?")

age = int(input("What age are you? "))
print("You entered ", age)

# We will edit this if statemnt to ensure they are also below 74
if (age >= 17 and age <= 74):
    print(name, "you are entitled to apply for a driving licence.")
# Now we need to check that they are above 74. 
elif (age >= 74):
    print(name, "you are entitled to apply for a three-year driving licence.")
# Since all the other cases are check we know they must be below 17
else:
    print(name, "you are not enitled to apply for a driving licenese")
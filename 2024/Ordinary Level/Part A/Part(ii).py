# Question 16(a)
# Examination Number:

# Insert a comment in the code that explains what is happening on line 6
# Line 6 from the code is:
# 
# 6 age = int(input("What age are you? "))
# 

print("Welcome to the driving licence eligibility checker")

# This is asking the user to input a response to the prompt:
# "What age are you?". It is converting your response to an int.
age = int(input("What age are you? "))

if (age >= 17):
    print("You are entitled to apply for a driving licence.")
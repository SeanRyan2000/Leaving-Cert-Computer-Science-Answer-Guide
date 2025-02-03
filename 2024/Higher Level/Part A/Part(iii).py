# Question 16(a)
# Examination Number:

# Add code to display the message “First fruit is cherry” if the first random fruit is a
# cherry

from random import choice

fruits = ['apple', 'cherry', 'orange']

random_fruit_1 = choice(fruits) 
random_fruit_2 = choice(fruits) 
random_fruit_3 = choice(fruits) 

print(random_fruit_1)
print(random_fruit_2)
print(random_fruit_3)

# Add if statement to check if the first fruit is cherry. 
# We are already declaring random fruit. So we will use the variable, random_fruit_1
if (random_fruit_1 == "cherry"):
    print("First fruit is cherry")
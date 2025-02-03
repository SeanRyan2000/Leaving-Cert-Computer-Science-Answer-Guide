# Question 16(a)
# Examination Number:

# Add code to display the message “First pair are cherries” if the first two fruits are both
# cherries. 

from random import choice

fruits = ['apple', 'cherry', 'orange']

random_fruit_1 = choice(fruits) 
random_fruit_2 = choice(fruits) 
random_fruit_3 = choice(fruits) 

print(random_fruit_1)
print(random_fruit_2)
print(random_fruit_3)

if (random_fruit_1 == "cherry"):
    print("First fruit is cherry")

if (random_fruit_1 == random_fruit_2):
    print("First pair match")

# Check if the first two fruit variables are both cherries
# There is multiple ways in which we can do the if statement. 
# This is probably the most intuitive.
if (random_fruit_1 == "cherry" and random_fruit_2 == "cherry"):
    print("First pair are cherries")
#  But we could also do something like
# if (random_fruit_1 == random_fruit_2 and random_fruit_1 == "cherry"):
#     print("First pair are cherries")

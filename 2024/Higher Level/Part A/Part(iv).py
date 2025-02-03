# Question 16(a)
# Examination Number:

# Add code to display the message “First pair match” if the first two fruits are the same.

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

# Check if the first two fruits are a match.
# We can use the two variables random_fruit_1 and random_fruit_2
if (random_fruit_1 == random_fruit_2):
    print("First pair match")
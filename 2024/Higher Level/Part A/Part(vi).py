# Question 16(a)
# Examination Number:

# Add code to display the message “Matching pair” if any two fruits are the same.

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

if (random_fruit_1 == "cherry" and random_fruit_2 == "cherry"):
    print("First pair are cherries")

# Check if there is any matching pair
# We could also do this in multiple ways. 
# The easiest is to check all combinations. 
# i.e., fruit1 == fruit2, fruit1 = fruit3, fruit2 == fruit3
# This is all possible combinations. It works well for this example. 
# 
# But what if we had a list of vars random_fruit_1, random_fruit_2, random_fruit_3 ... random_fruit_999
# 
# BONUS QUESTION: CAN YOU THINK OF A BETTER COMPARISON METHOD?
# Assume we have a list of the random fruits. 
# i.e., random_fruits = [choice(fruits) for _ in range(10)] 
# It would start getting complicated. 
# 
#

if (random_fruit_1 == random_fruit_2):
    print("Matching pair")
elif(random_fruit_1 == random_fruit_3):
    print("Matching pair")
elif(random_fruit_2 == random_fruit_3):
    print("Matching pair")


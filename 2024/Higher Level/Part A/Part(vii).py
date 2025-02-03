# Question 16(a)
# Examination Number:

# Extend the program with a loop that iterates 100 times. The loop should generate a
# random fruit on each iteration. After the loop is executed, the program should display
# a count of the number of times each fruit was generated. There is no need to display
# the names of the 100 fruits. 

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

if (random_fruit_1 == random_fruit_2):
    print("Matching pair")
elif(random_fruit_1 == random_fruit_3):
    print("Matching pair")
elif(random_fruit_2 == random_fruit_3):
    print("Matching pair")


 
# Create a new array for the fruits.
random_fruits = []
# Loop 100 times
for i in range(100):
    # Choose a random fruit and add it to the array
    random_fruit = choice(fruits)
    random_fruits.append(random_fruit)
for i in range(len(fruits)):
    # Use the built in count() method to count each fruit
    print(fruits[i], random_fruits.count(fruits[i]))
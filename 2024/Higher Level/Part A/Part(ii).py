# Question 16(a)
# Examination Number:

# Add statements to initialise two new variables with fruits chosen randomly from the
# list. You should also display the values of the variables which should be called
# random_fruit_2 and random_fruit_3.

from random import choice

fruits = ['apple', 'cherry', 'orange']

random_fruit_1 = choice(fruits) 
# Add new fruits 
# The choice method will randomly select a fruit from the list
random_fruit_2 = choice(fruits) 
random_fruit_3 = choice(fruits) 

print(random_fruit_1)
print(random_fruit_2)
print(random_fruit_3)
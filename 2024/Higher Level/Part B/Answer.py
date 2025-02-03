# Comment
# Examination number:

# import random choice so we can select random fruits from the list
from random import choice

# Initialize list
fruits = ["apple", "orange", "cherry"]

#Ask user for input. We are converting this to lowercase to follow the standard.
additionalFruit = input("Enter an additional fruit: ").lower()
# append the list with the new fruit 
fruits.append(additionalFruit)
# print fruits
print(fruits)

# Create a while loop prompting the user to keep entering their winning fruit
# once again we are converting to lowercase to match.
while True:
    userWinningFruit = input("Nominate your winning fruit: ").lower()
    if userWinningFruit not in fruits:
        print("Error, this is not in the list of fruits")
    else:
        print("The winning fruit you selected is", userWinningFruit)
        break

# Winning fruits, set up while loop
counter = 0
while True:
    counter += 1
    # Initialize an empty list.
    # This will get reset every time the while loop runs.
    randomFruits = []

    # Create 3 random fruits to add to the list
    for i in range(3):
        randomFruits.append(choice(fruits))

    # There is a lot of ways we could check if the random fruits are the same as the user selected fruit
    # We could use the count() method of randomFruits
    # if randomFruits.count(userWinningFruit) == 3:
    # 
    # We could use all()
    # if all(fruit == userWinningFruit for fruit in randomFruits):
    # 
    # Or we could check each fruit against our chosen fruit
    
    # initialize matched
    matched = 0
    # loop through each fruit
    for fruit in randomFruits:
        # if the fruit is the same as your chosen fruit increment matched
        if fruit == userWinningFruit:
            matched += 1
        # if the fruit is different break out of the for loop and restart the while loop
        else:
            break
    if matched == 3:
        print("Winner after", counter, "tries")
        break

    
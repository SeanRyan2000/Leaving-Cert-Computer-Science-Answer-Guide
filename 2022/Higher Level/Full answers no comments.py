# Question 16(a)
# Examination Number:
from random import randint

print("Dice simulation program")

results = []
frequencies = [0, 0, 0, 0, 0, 0]

for i in range (100):
    throw_result = randint(1,6) # store a random value between 1 and 6
    results.append(throw_result) # append each value to results

    if throw_result == 1:
        frequencies[0] = frequencies[0] + 1
    elif throw_result == 2:
        frequencies[1] = frequencies[1] + 1
    elif throw_result == 3:
        frequencies[2] = frequencies[2] + 1
    elif throw_result == 4:
        frequencies[3] = frequencies[3] + 1
    elif throw_result == 5:
        frequencies[4] = frequencies[4] + 1
    else:
        frequencies[5] = frequencies[5] + 1

print()

print ("Frequencies:", frequencies)

print("Value \t Frequency")
print("----- \t ---------")
for i in range(6):          # loop through  0->5 (number of sides on dice) 
    print(i+1, "\t", frequencies[i]) # print the value (0->5 + 1). This is the dice number. 

print()
print(frequencies.index(max(frequencies)) + 1, "was rolled the most, often (", max(frequencies), "times)")

print()
print("Bar chart")
print("---------")
for i in range(6):
    for j in range(frequencies[i]): # loop through the number of frequencies
        print("*", end="") # print a * for each frequency
    print()



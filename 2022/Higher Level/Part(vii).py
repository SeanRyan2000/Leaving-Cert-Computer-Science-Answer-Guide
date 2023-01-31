# Question 16(a)
# Examination Number:
from random import randint

print("Dice simulation program")

results = []
frequencies = [0, 0, 0, 0, 0, 0]

# Loop 100 times
for i in range (100):
    throw_result = randint(1,6) # store a random value between 1 and 6
    results.append(throw_result) # append each value to results

# Start to build up a list of frequencies for each value thrown
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

# print("Results:", results)

print ("Frequencies:", frequencies)

# display the frequencies in a table
print("Value \t Frequency")
print("----- \t ---------")
for i in range(6):          # loop through  0->5 (number of sides on dice) 
    print(i+1, "\t", frequencies[i]) # print the value (0->5 + 1). This is the dice number. 
            # Then using i (0->5) that will print the corresponding position of the frequency array


# There is several ways to do this. The cleanest way is to use the max() function
# This function will return the largest value in a list
# However you could also use a for loop to loop through the list and compare each value to the current largest value

print()
print(frequencies.index(max(frequencies)) + 1, "was rolled the most, often (", max(frequencies), "times)")


# 
# part (vii) start
#
print()
print("Bar chart")
print("---------")
for i in range(6):
    for j in range(frequencies[i]): # loop through the number of frequencies
        print("*", end="") # print a * for each frequency
    print() # print a new line

# 
# part (vii) end
#

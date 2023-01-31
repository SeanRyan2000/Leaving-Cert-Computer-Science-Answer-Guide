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

# 
# part (iv) start
# 
# all we are doing here is simmply commenting out the print statement
# we are still keeping the print statement above to format the whitespace
# this could also be accomplished by adding \n before the print statement for frequencies

# print("Results:", results)

# 
# part (iv) end
#

print ("Frequencies:", frequencies)

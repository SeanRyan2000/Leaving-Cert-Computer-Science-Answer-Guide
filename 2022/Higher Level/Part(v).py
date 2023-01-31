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


# 
# part (v) start
# 
# display the frequencies in a table
print("Value \t Frequency")
print("----- \t ---------")
for i in range(6):          # loop through  0->5 (number of sides on dice) 
    print(i+1, "\t", frequencies[i]) # print the value (0->5 + 1). This is the dice number. 
            # Then using i (0->5) that will print the corresponding position of the frequency array

# ALTERNATIVE SOLUTION 
# ignore this line
print("\n\nALTERNATIVE SOLUTION\n")
# end of ignore this line

print("Value \t Frequency")
print("----- \t ---------")
print("1 \t", frequencies[0])
print("2 \t", frequencies[1])
print("3 \t", frequencies[2])
print("4 \t", frequencies[3])
print("5 \t", frequencies[4])
print("6 \t", frequencies[5])


# 
# part (v) end
# 
# Question 16(a)
# Examination Number:
from random import randint


# 
# PART(i) start
# 
# Change this line from 
# print("Dice simulation and analysis")
# to
print("Dice simulation program")
#
# PART(i) end
# 

results = []
frequencies = [0, 0, 0, 0, 0, 0]

for i in range (100):
    throw_result = randint(1,6) # store a random value between 1 and 6
    results.append(throw_result) # append each value to results 

    if throw_result == 1:
        frequencies[0] = frequencies[0] + 1
    elif throw_result == 2:
        frequencies[1] = frequencies[1] + 1
# 
# part (iii) start
# 
    # continue the if else statement to add the frequencies for the other values
    elif throw_result == 3:
        frequencies[2] = frequencies[2] + 1
    elif throw_result == 4:
        frequencies[3] = frequencies[3] + 1
    elif throw_result == 5:
        frequencies[4] = frequencies[4] + 1
    else:
        frequencies[5] = frequencies[5] + 1
    # Notice the else statement instead of elif throw_result == 6:
    # This is because the only other possible value is 6
    # so we dont need to waste resources checking it
#
# part (iii) end
#

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

# 
# PART(ii) start
# 
# add this line of code to the program to print the array of frequencies
print ("Frequencies:", frequencies)
#
# PART(ii) end
# 



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

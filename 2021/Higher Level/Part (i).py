# Question 16(a)
# Examination Number:

# function definition used in part (v)
def is_anagram(w1, w2):
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False

word1 = input("Enter the first word: ") 

# 
# PART(i) start
# 

# Change word 2 to be a user input like word1 
word2 = input("Enter the second word: ")
#
# PART(i) end
# 


if (sorted(word1) == sorted(word2)) :
    print("YES")


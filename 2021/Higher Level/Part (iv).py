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
# word2 = "SILENT" 
word2 = input("Enter the second word: ")
#
# PART(i) end
# 


# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams


#
# PART (iv) start
#
# if (sorted(word1) == sorted(word2))
# change the case of both the variables word1 and word2 to lower case so the case wont matter
if (sorted(word1.lower()) == sorted(word2.lower())) :
#
# PART (iv) end
#

#
# PART (ii) start
#
# Change "YES" to include the 2 variables word1 and word2 and input the text between them
# print("YES")
    print(word1 + " is an anagram of " + word2)

#
# PART (ii) end
#

#
# PART (iii) start
#
# nothing here must write all new code
# else in case it fails the if statement 

else: 
    print(word1 + " is NOT an anagram of " + word2)
#
# PART (iii) end
#






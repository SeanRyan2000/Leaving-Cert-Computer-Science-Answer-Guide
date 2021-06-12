# Question 16(a)
# Examination Number:

# function definition used in part (v)
def is_anagram(w1, w2):
    if sorted(w1) == sorted(w2):
        print(word1 + " is an anagram of " + word2) # added in for part (v)
        return True
    else:
        print(word1 + " is NOT an anagram of " + word2) # added in for part (v)
        return False

#
# function definition for (vi) START
#

def is_anagram_phrase(w1,w2,w3):
    w3 = w3.replace(" ", "") # Get rid of the spaces in the variable w3
    if sorted(w3) == sorted(w1): 
        print(word1 + " is an anagram of " + w3) # Use w3 (no spaces) if it is an anagram
    else:
        print(word1 + " is NOT an anagram of " + word3) # Keep the spaces if it is not an anagram
        
    if sorted(w3) == sorted(w2):
        print(word2 + " is an anagram of " + w3) # Use w3 (no spaces) if it is an anagram
    else:
        print(word2 + " is NOT an anagram of " + word3) # Keep the spaces if it is not an anagram
            
#
# function definition for (vi) END
#

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

#
# PART (v) start
#
is_anagram(word1.lower(), word2.lower())

# Go to Line 7 and 10
# PART (v) end
#

#
# PART (vi) start
#

word3 = input("\nEnter a phrase: ")
is_anagram_phrase(word1.lower(), word2.lower(), word3.lower())

# go to function is_anagram_phrase
#PART (vi) end
#



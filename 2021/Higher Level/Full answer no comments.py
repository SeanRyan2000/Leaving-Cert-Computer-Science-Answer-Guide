# Question 16(a)
# Examination Number:
def is_anagram(w1, w2):
    if sorted(w1) == sorted(w2):
        print(word1 + " is an anagram of " + word2) 
        return True
    else:
        print(word1 + " is NOT an anagram of " + word2) 
        return False

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

word1 = input("Enter the first word: ") 
word2 = input("Enter the second word: ")

if (sorted(word1.lower()) == sorted(word2.lower())) :
    print(word1 + " is an anagram of " + word2)
else: 
    print(word1 + " is NOT an anagram of " + word2)

is_anagram(word1.lower(), word2.lower())
word3 = input("\nEnter a phrase: ")
is_anagram_phrase(word1.lower(), word2.lower(), word3.lower())
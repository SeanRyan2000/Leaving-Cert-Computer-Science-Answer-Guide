# Question 16 (a)
# Examination Number:


firstName = input("What is your first name? ")

# 
# Part (ii) start
# 
# We are copying the line above and changing the variable name to surname. 
# Similiarly we will change the text asked to what is your surname
surname = input("What is your surname? ")
# 
# Part (ii) end
# 

print("Hello", firstName)


print("Please select from the list of items.\n")
# \n creates a new line
print("\tItems Available") # \t creates a tab
print("1 = Book")

shoppingItem = int(input("\nEnter the number of the item you would like: "))

if shoppingItem == 1:
    print("You bought a book")
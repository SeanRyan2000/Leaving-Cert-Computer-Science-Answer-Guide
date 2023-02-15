# Question 16 (a)
# Examination Number:

# 
# Part (i) start
# 
# This is the line that you enter your name. The input() function will wait for the user to enter a value. 
# The value is then stored in the variable firstName
firstName = input("What is your first name? ")
# 
# Part (i) end
# 
print("Hello", firstName)


print("Please select from the list of items.\n")
# \n creates a new line
print("\tItems Available") # \t creates a tab
print("1 = Book")

shoppingItem = int(input("\nEnter the number of the item you would like: "))

if shoppingItem == 1:
    print("You bought a book")
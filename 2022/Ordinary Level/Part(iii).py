# Question 16 (a)
# Examination Number:


firstName = input("What is your first name? ")
surname = input("What is your surname? ")

# 
# Part (iii) start
# 

# We are now going to change the print statement to include the surname
print("Hello", firstName, surname)

# 
# Part (iii) end
# 


print("Please select from the list of items.\n")
# \n creates a new line
print("\tItems Available") # \t creates a tab
print("1 = Book")

shoppingItem = int(input("\nEnter the number of the item you would like: "))

if shoppingItem == 1:
    print("You bought a book")
# Question 16 (a)
# Examination Number:


firstName = input("What is your first name? ")
surname = input("What is your surname? ")

print("Hello", firstName, surname)


print("Please select from the list of items.\n")
# \n creates a new line
print("\tItems Available") # \t creates a tab

# 
# Part (iv) start
# 
print("1 = Book")
# we are adding a ruler and a pen to the list of items available
# it will now print 3 items, book, ruler and pen
print("2 = Ruler")
print("3 = Pen")
# 
# Part (iv) end
# 
shoppingItem = int(input("\nEnter the number of the item you would like: "))

if shoppingItem == 1:
    print("You bought a book")

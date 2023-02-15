# Question 16 (a)
# Examination Number:


firstName = input("What is your first name? ")
surname = input("What is your surname? ")

print("Hello", firstName, surname)


print("Please select from the list of items.\n")
# \n creates a new line
print("\tItems Available") # \t creates a tab

print("----------------------")
print("1 = Book")
print("2 = Ruler")
print("3 = Pen")
print("----------------------")

shoppingItem = int(input("\nEnter the number of the item you would like: "))

if shoppingItem == 1:
    print("You bought a book")
elif shoppingItem == 2:
    print("You bought a ruler")
elif shoppingItem == 3:
    print("You bought a pen")

# 
# Part (vii) start
#
# We are using an else statement as it will handle anything that is not 1, 2 or 3.
else:
    print("Invalid choice. Goodbye.")
#
# Part (vii) end
#
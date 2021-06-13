# Question 16(a)
# Examination Number:

# (iii) create a boolean variable loggedIn set to false
loggedIn = False

# (vi) create a variable failedAttempts with initial value of 0
failedAttempts = 0


pin = "1579"

# (v) while loop
# continues to run if logged in is false, runs first time due to initial state of logged in
# will then continue until you get it right due to if userTry == pin    loggedIn gets set to true


# (vii) we are editing the while loop to contain another check
# only run if logged in is false and failedAttempts is less than 3

while (loggedIn == False and failedAttempts < 3):
    
    userTry = input("Enter PIN:") # (i) The input command is asking the user to type in their Pin code.



    if userTry == pin:
    # (iv) change loggedIn's state to true
        loggedIn = True
        print("Welcome")
    else :
        print("Incorrect PIN ")
        # (vii) increment failed attempts
        failedAttempts = failedAttempts + 1


    # create an if statement for if failedAttempts is equal to 3
    # (vii)
    if (failedAttempts == 3) :
        print("You have entered the PIN incorrectly 3 times.")        



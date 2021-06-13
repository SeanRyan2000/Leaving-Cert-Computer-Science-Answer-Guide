# Question 16(a)
# Examination Number:


loggedIn = False

failedAttempts = 0


pin = "1579"

while (loggedIn == False and failedAttempts < 3):
    
    userTry = input("Enter PIN:")

    if userTry == pin:
        loggedIn = True
        print("Welcome")
    else :
        print("Incorrect PIN ")
        failedAttempts = failedAttempts + 1

    if (failedAttempts == 3) :
        print("You have entered the PIN incorrectly 3 times.")        



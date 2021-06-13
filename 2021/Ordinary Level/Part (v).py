# Question 16(a)
# Examination Number:

# (iii) create a boolean variable loggedIn set to false
loggedIn = False

pin = "1579"

# (v) while loop
# continues to run if logged in is false, runs first time due to initial state of logged in
# will then continue until you get it right due to if userTry == pin    loggedIn gets set to true
while (loggedIn == False): 
    
    userTry = input("Enter PIN:") # (i) The input command is asking the user to type in their Pin code.



    if userTry == pin:
    # (iv) change loggedIn's state to true
        loggedIn = True
        print("Welcome")
    else :
        print("Incorrect PIN ")


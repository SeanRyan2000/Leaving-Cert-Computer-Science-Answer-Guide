# Comment
# Examination number:

# Display the message Welcome to Temperature Alert System
print("Welcome to Temperature Alert System")

# Ask the user to enter a temperature value in degrees Celsius
temperature = int(input("Enter temperature value in degrees Celsius: "))

# Use the table and add conditional (if) statements
if temperature < 20:
    print("Too cold. Turn up heating.")
# This if statement is just checking if the temperature is less than or equal 24
# This is because in the previous statement we are checking that it is above 20
elif temperature <= 24:
    print("Temperature is just right.") 
elif temperature > 24:
    print("Too warm. Turn down heating.")
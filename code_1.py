# Getting User Input
# Input value entered will return a string type

# name = input("Please enter you name: ")
# age = input("Please enter you age: ")
# print(f"Hi {name}, you are {age} years old")

# Mathematic operation from input
sizeInput = input("How bis is your house (in squares feet): ")
squareMeter = int(sizeInput) / 10.8    #converting sting into int (a number)
print(f"Square feet: {sizeInput} is {squareMeter:.2f} square meters") #Show the number for 2dp (.2f)

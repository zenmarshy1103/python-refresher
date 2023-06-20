# Loops in Python

number = 7


#While Loop
# Conditional

# while True: #indefinate Loop
#     user_input = input("Would you like to play? (Y/n)")

#     #Check if input is n, if it is terminate the while loop
#     if user_input == "n":
#         break

#     user_number = int(input("Guess a number: "))
#     if user_number == number:
#         print("You got it correct")
#     elif number - user_number in (1, -1):   #make a tuple to check if the condition is one of the two in the tuple
#         print("you were off by 1")
#     else:
#         print("It is wrong")
   

#For Loop
# Iterative

friends = ["Cyrus", "Claire", "Clara", "Jason", "Faye"]

for friend in friends:  #friend gets the index of the list
    print(f"{friend} is one of my friends")

grades = [25, 50, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade
    
print("The average for this class is: ", total / amount)    
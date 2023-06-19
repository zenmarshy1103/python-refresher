# >> Boolean
# Made up of comparison 
# print(5 == 5) 
# print(10 != 10)
# print(5 > 4)
# print(6 < 9)

#Keywords to calculate Boolean
friends = ["Nick", "Wilson"]
abroad = ["Nick", "Wilson"]

# print(friends == abroad)  #check if the elements are the same
# print(friends is abroad)  #checks the area in the memory. exact same thing in the memory

# >> If Statement 
# Allow us to use boolean to do certain operation
# day_of_day = input("What day of the week is it today? ").lower()  #turn the input to lowercase using .lower()

# if day_of_day == "monday":    # IF-ELSE If-ELSE Statement SYNTAX
#     print("true")
# elif day_of_day == "sunday":
#     print("Enjoy your Sunday")
# else:
#     print("Enjoy your day")

# >> The "in" Keyword
# Check if a thing is inside a list, tuple, set and string
# friends = ["Jen", "Claire", "Clara", "Cyrus"]
# print("Cyrus" in friends)  #Check if Cyrus is inside the friends list

# movies_watched = {"Demon Slayer", "Mashel", "Bleach"}
# print("Bleach" in movies_watched)

# >> If statement with "in" keyword
# user_movie = input("Enter something you have watched recently: ")

# if user_movie in movies_watched:
#     print(f"I have watched {user_movie} too!")
# else:
#     print("I have not watched that yet.")


# Guess Number Game
number = 7
user_input = input("Enter 'y' to play ")

# if user_input == "y":
# Use in keyword
if user_input in ("y", "Y"):   #making a tuple of values to only allow - check if the user input is one of the two in the tuple
    user_number = int(input("Guess a number: "))
    if user_number == number:
        print("You got it correct")
    elif number - user_number in (1, -1):   #make a tuple to check if the condition is one of the two in the tuple
        print("you were off by 1")
    else:
        print("It is wrong")



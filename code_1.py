# Functions 
# Are callable variable that is defined by you
# Defining our own function
# Can reuse functions
# Can use Global and Function Scope Variables

# Function without return 
# Defining the code
def hello():
    print("Hello!")
  
# Running the code    
hello()

def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60   
    print(age_seconds)
    
user_age_in_seconds()

# Using global scope varaible 
friends = ["Jason", "Bob"]  

def add_friend():
    friend_name = input("Enter your friend's name: ")
    friends.append(friend_name)

add_friend()    
print(friends)




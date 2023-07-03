# Dictionary Comprehension
#   - returns a dictionary with key-value pairs
#   <SYNTAX>
#       {key:value for index in list }

# A list with tuples stored in it
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

# Dictionary Comprehension: 
#   - Adding key-Value pairs onto a new dictionary
#   <SYNTAX>
#       {key:value for index in list }

username_mapping = {user[1]: user for user in users} # Getting {"BoB": (0, "Bob", "password")} ...
print(username_mapping)

# same as 
mapping_users = {}  # Need to create an empty dictionary to put key-value pairs in

for user in users:
    mapping_users[user[1]] = user 
    
print(mapping_users)

# REAL-WORLD CASE: Checking login (username and password)    

# Since username_mapping is:
#{'Bob': (0, 'Bob', 'password'), 
# 'Rolf': (1, 'Rolf', 'bob123'), 
# 'Jose': (2, 'Jose', 'longp4assword'), 
# 'username': (3, 'username', '1234')}
print(username_mapping.keys())

#inputs for users
username_input = input("Enter your username: ")
password_input = input("Enter you password: ")

# check if the user input is contained in the dictionary 
if username_input in username_mapping.keys():
    # Destructure the value when calling the key to username and password and ignoring the 1st value
    _, username, password = username_mapping[username_input]

    if  password_input == password:
        print("Logging in")
    else:
        print("Try again")
else:
    # Output this line when the user input is not contained dictionary
    print("Please inform IT")
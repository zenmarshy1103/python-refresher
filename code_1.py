# functions - Unpacking Keyword Arguments 
#   - **kwargs unpacks arguments and store them in a kwarg dictionary
#   - arguments passed in **kwargs must be a dictionary
#   - ** can be used for destructing(unpack) a dictionary

def named(**kwargs):  # ** collects keyword arguments and put it into a dictionary
    print(kwargs)
    
named(name="jason", age=23)

# Using destructing on the dictionary and turn the properties into the parameters that the function parameter list contain
def name(name, age):
    print(name, age)

#   - Dictionary
details = {
    "name": "Bob",
    "age": 25
}

# destructuring dictionary
#   <SYNTAX> **dictionary

#calling the name function and place the destructuring dictionary as the argument of the function
name(**details)  

def print_nicely(**kwargs):
    #<Note> **kwargs collects the keyword argument and store them in a dictionary called kwarg
    named(**kwargs) # here the argument to the calling function destructure the kwarg dictionary and passed in the named arguments
    # Destructuring the kwarg (dictionary) into arg and value and print them out
    for arg, value in kwargs.items(): # Kwarg here gets the dictionary collected by the **kwargs from the print_nicely parameter list
        print(f"{arg}: {value}")
        
print_nicely(named="Bob", age=25)


def both(*args, **kwargs):
    #   - *args collects all the positional arguments and store them in a arg tuple
    print(args)
    #   - **kwargs collects all the named arguments and store them in a kwarg dictionary
    print(kwargs)

both(1, 3, 5, name="Jason", age=25)

def myfunction(**kwargs):
    print(kwargs)
    
# <REMEMBER>
#   what is passed into **kwarg must be a dictionary of it will come up with an error


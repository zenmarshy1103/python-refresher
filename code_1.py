# Functions - Arguments and Parameters

# Function with Parameter
def add(x, y):   # x and y are Parameters
    result = x + y
    print(result)
    
    
add(5, 3)      #5 and 3 are argument going into the add() function

def say_hello(first_name, last_name):
    print(f"Hello {first_name} {last_name}")

#Positional Argument: each argument corresponds to the position of the  parameters defined in the ()    
say_hello("Jason", "Liu") 

# Not Positional Argument: keyword or Named arguments
# Always use keyword arguments in python
say_hello(last_name="Jia", first_name="Faye")

 
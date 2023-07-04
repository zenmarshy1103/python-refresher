# Function - Unpacking Arguments
#
#
#

# Collecting multiple arguments using *args
#   - args can be any name (just a convention)
def multiply(*args):
    """This function has a set of arguments that will be collected into a tuple of args when the function gets called"""
    total = 1
    print(args)
    #using For Loop to multiply each value in the tuple together
    for arg in args:
        total = total * arg      #1st iteration: total = 1  * 1  (total = 1)
                                 #2nd iteration: total = 2 * 3 (total = 3)
                                 #3rd iteration: total = 3 * 5 (total = 15)
    return total           
    

print(multiply(1, 3, 5))

# Destructuring arguments to the number of parameter in the function parameter list
#   - make sure the number of argument equals the function parameter list
def add(x, y):
    return x + y

num = [3, 5]
print(add(*num))  #this destructure the values stored in num into the parameter value of x and y ( now x = 3, y = 5)

# Passing in dictionary as arguments using **nums and associate each key to the parameter of the function

nums = {
    "x": 15,
    "y": 25,
}

# - Normal way
print(add(x=nums["x"], y=nums["y"]))

# - Alternative way using **nums
print(add(**nums))

def apply(*args, operator):  #collect all the positional argument into args tuple and also have an named argument for operator at the end
    
    if operator == "*":
        # return multiply(args) #in this case the args tuple is being passed into the multiply function
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to function apply()"
    

print(apply(1, 1, 2, 1, operator="*"))   # args = ((1, 1, 2, 1),)  operator="*"  so have to change the argument passed into multiply function in the apply function to *args

print(apply(1, 1, 1, 1, operator="+"))
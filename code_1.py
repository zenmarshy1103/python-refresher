# Functions - Lambda Functions
#   - A function that does not have a name but used to return values
#   - Used to operate on input and return output, never used to perform actions  
#   - Using a list Comprehension as argument 
#   - Alternative to using list comprehension as arguments use map()

# Lambda Function
#   - We do not specify the return keyword
#   - <SYNTAX>  lambda arg_1, arg_2 : return value
add = lambda x, y: x + y

print(add(5, 7))

def double(x):
    return x  * 2

# Using List Comprehension as the argument
#   - List Comprehension returns a new list
sequence = [1, 2, 4, 6]
doubled = [double(x) for x in sequence]
print(doubled)

# Using Map Function on list
#   - Loop over a list and does a function over a list
#   - In Python map returns a map object, to use it need to turn in into a list first list(map())
#   - <SYNTAX> map(function, iterable)
doubled_map = list(map(double, sequence))
print(doubled_map)

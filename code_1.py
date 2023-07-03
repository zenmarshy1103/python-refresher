# Functions - Default Parameter Values
# Default Parameter must be at the end of the parameter list ()

# Setting Default Values
def add(x, y=8):   # x is a required parameter, y is set as default with 8
    print(x + y)

add(1)
add(x=5)
add(x=5, y=1)  # re-assiging y with new argument value which overwrites the default





 
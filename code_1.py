# Functions - Returning Values

# Function without return
#   - will return None by default
def add(x, y):
    print(x + y)
    
add(5, 8)

# Function with return
#   - will return the value specified

def addition(x, y):
    return x + y

sum = addition(5, 8)
print(sum)


def divide(divident, divisor):
    if divisor !=0:
        return int(divident / divisor)
    else:
        return "you fool!"
    
result = divide(15, 3)
print(result)





 
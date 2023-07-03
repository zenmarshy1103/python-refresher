# Destructing Variables 

# tuples (The () is not needed but will needed if you put a tuple inside a list)
x = 5, 11
print(type(x))

# Destructure a tuple with valuables assigned to each value in the tuple
x, y = 4, 22
print(x)
print(y)

student_attendance = {
    "Jason": 100,
    "Cyrus": 100,
    "Oreo": 50,
}

#Turning dictionary into a list
print(list(student_attendance.items()))  # <NOTE> the dictionary items are turned into tuples and stored in the list 

# Iterate through each of the tuples in the list and destructure into three separate categories
people = [("Bob", 42, "Mechanics"), ("James", 24, "Artest"), ("Harry", 32, "Lecturer")]

for name, age, job in people:  # iterate over people to destructure into name age and job
    print(f"Name: {name}, Age: {age}, Job: {job}")
  
  
# Ignore a value in destructuring
person = ("Jason", 34, "Front End Developer")
name, _, profession = person    # _ is ignored
print(name, profession)  
    
    
# Destructure a list
author = ["Jason", 23]
name, age = author
print(name)
print(age)

# Destructuring the remaining values
head, *tail = [1, 2, 3, 4, 5]   # *tail will collect all of the destructuring values into this variable
print(head)
print(tail)

*head, tail = [5, 4, 3, 2, 1] # *head will collect all the front until the one before the last one
print(head)
print(tail)



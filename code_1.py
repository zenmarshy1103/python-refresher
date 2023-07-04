# Object Oriented Programming


student = {
    "name": "Rolf",
    "grades": (89, 90, 93, 78, 90),
}
# Function 
def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))


# Object Oriented Programming
#   - Allows us to get information in regards to which student ie rolf.average (using the method inside the object)

# Initialise class
class Student:
    # Init method: for setting the class's properties
    def __init__(self, name, grades):  # A parameter must be existing for init method, self: so the methods can take in the object that you have been constructing
        # self.name = "rolf"
        self.name = name    # when here are more than one parameter in the method parameter list, the parameter can be used just like a function parameter list
        self.age = 23
        self.grades = grades
        
    # Defining method inside the class, will take self as parameter (convention in Python)  -- self does not need to be named as it is.
    def average_grades(self):   #the parameter must be the object that was created initially
        return sum(self.grades) / len(self.grades)   
     

# Create an object that behaves exactly as the initialized class      
# student = Student()   #calls the init method in the class and creates this empty thing called self and inside self has the name and age variable set in the method
# print(student.name)

#Putting in argument for the class to create an object with name and grade arguments
rolf = Student("Rolf", (100, 100, 93, 78, 90))
print(rolf.name)
#calling method in the object
print(rolf.average_grades())

#Creates another object
bob = Student("Bob", (55, 60, 99, 100, 100))


print(Student.average_grades(bob))  #using the student class to call the average_grades method on the bob object

# simpler way to calling method on the object
#   - Use the object that is created and call the method in it ( the object has the blue print of the class the "self" - refers to the object created by the class itself)
print(bob.average_grades())






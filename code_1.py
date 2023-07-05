# Object Oriented Programming - Magic Methods: _ _str _ _ and _ _ repr _ _
#   - Special Methods: _ _ method _ _ will be called by python automatically at times
#   - These two method is used for representing an object (Not compulsory to use)

class Person:
    def __init__(self, name, age): # Special (Magic) Method
        # The method gives us an empty object called self
        
        #setting the name and age properties of the empty object (self)
        self.name = name 
        self.age = age
        
    # A special method that turns your object into a string representation
    #   - To print out nice and easy to read string to users     
    # def __str__(self):
    #     return f"This Person {self.name}, {self.age} years old"
    
    # A special method that is used to tell programers to read the string here that we are printing out an object
    #   - Should return a string that allows us to recreate the original object with ease
    #   - to display this make sure the __str__ method is commented or not present or python will print out the __str__ not the __repr__ method
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"
        
        
        
    
jason = Person("Jason", 34)  # When creating an object from the class, python calls the __init__ method even when you didn't call it
print(jason)



# Object Oriented Programming - Class Methods and Static Methods
#   - 

# Instance Method
#   - Method inside a class
class ClassTest:
    def instance_method(self): #self will be the instance or the object 
        print(f"Called instance_method of {self}")
        
    @classmethod
    def class_method(cls):  #cls will be the class itself in this case cls will be the ClassTest class
        print(f"Called class_method of {cls}")
        
    @staticmethod  
    def static_method():   # Does not need an argument at all 
        print("Called Static_method")
        

# Calling instance method
#   Method One
test = ClassTest()
test.instance_method()

#   Method Two
# ClassTest.instance_method(test)

# Calling class method
ClassTest.class_method()

# Calling Static Method
ClassTest.static_method()


#Factory Example (Class Method)

class Book:
    TYPES = ("hardcover", "paperback")  #property for the class
    
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighting {self.weight}grams>"
    
    @classmethod
    def hardcover(cls, name, page_weight):   # cls is book class hence can use cls 
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):  # Using the class name also works (Book)
        return Book(name, Book.TYPES[1], page_weight)
    

#Creating an instance of book
book = Book("Harry Porter", "hardcover", 1500)
print(book)

#Creating an instance and calling classmethod
book = Book.hardcover("Demon Hunter", 500)
print(book)

book_1 = Book.paperback("Bleach", 300)
print(book_1)        
    
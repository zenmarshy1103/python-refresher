# Object Oriented Programming - Class Composition
#   Counter Part to Inheritance:  To build out classes using other classes
#       - This is used much more than inheritance 
#   Use Composition: when you are not going to use the inherited properties methods etc.
# <Theory>
#   - Inheritance: Book is a bookshelf
#   - Composition: A bookshelf has many books 


# class BookShelf:
#     def __init__(self, quantity):
#         self.quantity = quantity
        
#     def __str__(self):
#         return f"BookShelf with {self.quantity} books"

class BookShelf:
    def __init__(self, *books): # *books will take in a bunch of book objects
        self.books = books
    
    def __str__(self):
        return f"BookShelf with {len(self.books)} books."
    
class Book:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"Book {self.name}"
        


# Creating book instances
book = Book("Harry Porter")
book1 = Book("Python 101")
shelf = BookShelf(book, book1)

print(book)
print(shelf)






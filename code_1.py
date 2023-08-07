# Object Oriented Programming - Class Inheritance
#   Inheritance: Allows one class to take some methods and properties from another class
#   Hierarchy of calling (if method cannot be found):
#       - 1st: calling in current class
#       - 2nd: Parent class (if current class is inheriting from parent class)
#       - 3rd: Object Class
#       - if it does not exist in any of the above, an error will be prompted

class Device:
    def __init__(self, name, connected_by):
         self.name = name 
         self. connected_by = connected_by
         self.connected = True
         
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"   # !r - calls the repr method of self.name (in this case) amd shows up with the quotes around it ' '
    
    def disconnect(self):
        self.connected = False
        print("Disconnected.")
        
        
printer = Device("printer", "USB")
print(printer)
printer.disconnect()

# Inheritance 
#   - Creating a printer class which has all the methods and properties of the device class plus its own printing methods

class Printer(Device): #create a printer class and it inherits from device
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)   #super() gets the super class (Parent Class) in this case it will be the device class
        self.capacity = capacity   # <- Maximum Capacity of the the printer 
        self.remaining_pages = capacity # <- Current Capacity of the printer 
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return 
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages
        
#Create a new printer class with printer as variable
printer = Printer("Printer", "USB", 500)

#calling the print method inside the printer class
printer.print(20)
print(printer)
printer.disconnect()


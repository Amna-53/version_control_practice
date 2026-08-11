# Single Inheritance:
# parent class
class Parent: 
   def parentMethod(self):
      print ("Calling parent method")

class Child(Parent): # child class
   def childMethod(self):
      print ("Calling child method")
# instance of child
c = Child()  
# calling method of child class
c.childMethod() 
c.parentMethod() # calling method of parent class

c.childMethod() 
c.parentMethod() # calling method of parent class


# Multi_Level Inheritance:
# Parent class
class Bank:                                 # Create the parent class
    def bankMethod(self):                   # Define a method in the Bank class
        print("This is a Bank")             # Display a message
# Child class
class Account(Bank):                        # Account inherits from Bank
    def accountMethod(self):                # Define a method in the Account class
        print("This is an Account")         # Display a message
# Grandchild class
class Savings(Account):                     # Savings inherits from Account (and indirectly Bank)
    def savingsMethod(self):                # Define a method in the Savings class
        print("This is a Savings Account")  # Display a message

# Create object
s = Savings()                               # Create an object of the Savings class

# Call methods
s.bankMethod()                              # Calls the inherited method from Bank
s.accountMethod()                           # Calls the inherited method from Account
s.savingsMethod()                           # Calls the method of the Savings class


 # combined single and multiple inheritance to form a hybrid inheritance of classes.
# Parent class
class CEO:                                    # Create the parent class
    def ceoMethod(self):                      # Define a method in the CEO class
        print("I am the CEO")                 # Display a message

# Child class
class Manager(CEO):                           # Manager inherits from CEO
    def managerMethod(self):                  # Define a method in the Manager class
        print("I am the Manager")             # Display a message
# Child class
class Employee1(Manager):                     # Employee1 inherits from Manager
    def employee1Method(self):                # Define a method in the Employee1 class
        print("I am Employee one")            # Display a message

# Another child class
class Employee2(Manager, CEO):                # Employee2 inherits from Manager and CEO
    def employee2Method(self):                # Define a method in the Employee2 class
        print("I am Employee two")            # Display a message

# Creating an object
emp = Employee2()                             # Create an object of the Employee2 class

# Calling methods
emp.managerMethod()                           # Calls the inherited method from Manager
emp.ceoMethod()                               # Calls the inherited method from CEO
emp.employee2Method()                         # Calls the method of the Employee2 class


# Hierarchical Inheritance:
# Parent class
class Vehicle:                              # Create the parent class
    def vehicleMethod(self):                # Define a method in the Vehicle class
        print("This is a Vehicle")          # Display a message

# Child class
class Car(Vehicle):                         # Car inherits from Vehicle
    def carMethod(self):                    # Define a method in the Car class
        print("This is a Car")              # Display a message
# Another child class
class Bike(Vehicle):                        # Bike inherits from Vehicle
    def bikeMethod(self):                   # Define a method in the Bike class
        print("This is a Bike")             # Display a messagepractice
# Create objects
c = Car()                                   # Create an object of the Car class
b = Bike()                                  # Create an object of the Bike class
# Call methods
c.vehicleMethod()                           # Calls the inherited method from Vehicle
c.carMethod()                               # Calls the method of Car class

b.vehicleMethod()                           # Calls the inherited method from Vehicle
b.bikeMethod()                              # Calls the method of Bike class

# create a parent class and access its constructor from a subclass using the super() function
# Parent class
class ParentDemo:                               # Create the parent class
    def __init__(self, msg):                    # Constructor of the parent class
        self.message = msg                      # Store the message in an instance variable

    def showMessage(self):                      # Define a method to display the message
        print(self.message)                     # Print the stored message
# Child class
class ChildDemo(ParentDemo):                    # ChildDemo inherits from ParentDemo

    def __init__(self, msg):                    # Constructor of the child class
        super().__init__(msg)                   # Call the parent class constructor using super()
# Creating an object
obj = ChildDemo("Welcome to Tutorialspoint!!")  # Create an object of the ChildDemo class

# Calling method
obj.showMessage()                               # Call the inherited method to display the message
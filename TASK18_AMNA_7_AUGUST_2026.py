# LIST COMPREHENSION:
# Create a list of numbers from 1 to 5
numbers = [x for x in range(1, 6)]
print(f"Numbers:{numbers}")  #  print the numbers


# Create a list containing squares of numbers from 1 to 5:
squares = [x * x for x in range(1, 6)]
print(f" Square of numbers:{squares}")   # display square of numbers

# Create a list of even numbers from 1 to 10:
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even Numbers:{even_numbers}")  # display the even numbers 

# Create a list of odd numbers from 1 to 10
odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print(f"Odd Numbers:{odd_numbers}")  # display the odd numbers


# Convert strings to uppercase:
names = ["amna", "ali", "sara"]
upper_names = [name.upper() for name in names]  # Convert every name to uppercase
print(f"Strings to upper_case:{upper_names}")  # display the uppercase names

# Convert string to lowercase:
names = ["AMNA", "ALI", "SARA"]
lower_names = [name.lower() for name in names]  # Convert every name to lowercase
print(f"Strings to Lower_case:{lower_names}")  #  display the lowercase names

# List comprehension with if_else:
numbers = [1, 2, 3, 4, 5]
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers] # Put "Even" for even numbers and "Odd" for odd numbers
print(f"Condition check_out{result}") # display the result 

# Extract fisrt letter:
names = ["Amna", "Ali", "Sara", "Ahmed"]
first_letters = [name[0] for name in names] # Get the first letter of every name
print( f"Extract fisrt_letters:{ first_letters}")  #  Display the first letter of each name

# create a list of cubes:
# Create cubes of numbers from 1 to 5
cubes = [x ** 3 for x in range(1, 6)]
print(f"List of Cubes:{cubes}")  # display the cube of numbers



# Decorators:
# Decorator function
def my_decorator(func):
    # Wrapper function
    def wrapper():
        print("Before function")   # Code that runs before the original function
        func()                     # Call the original function
        print("After function")    # Code that runs after the original function
    return wrapper                # Return the wrapper function
# Applying decorator
@my_decorator
def hello():
    print("Hello World")           # Original function
hello()                            # Call the decorated function


#  Apply decorators manually:
# Decorator function
def my_decorator(func):                 # Create decorator function
    def wrapper():                       # Create wrapper function
        print(f"Starting")               # Runs before the function
        func()                           # Calls the original function
        print(f"Ending")                 # Runs after the function
    return wrapper                       # Return wrapper

# Normal function
def greet():                             # Create normal function
    print(f"Hello")                      # Print Hello
# Apply decorator manually
greet = my_decorator(greet)              # Apply decorator to greet
greet()                                  # Call decorated function

# Decorator with arguments:
# Decorator function
def my_decorator(func):                  # Create decorator function
    def wrapper(name):                   # Wrapper accepts name
        print(f"Function started")       # Runs before the function
        func(name)                       # Calls original function
        print(f"Function ended")         # Runs after the function
    return wrapper                       # Return wrapper

# Apply decorator
@my_decorator                            # Apply decorator
def greet(name):                          # Create function with name
    print(f"Hello {name}")                # Print the name
greet("Amna")                             # Call function with argument



# Login Check:
# Decorator function
def login_required(func):                # Create login decorator
    def wrapper(is_logged_in):            # Wrapper accepts login status
        if is_logged_in:                  # Check if user is logged in
            func()                        # Call original function
        else:
            print(f"Please login first")  # Show message if not logged in
    return wrapper                       # Return wrapper
# Apply decorator
@login_required                           # Apply login decorator
def dashboard():                          # Create dashboard function
    print(f"Welcome to dashboard")        # Show dashboard
dashboard(True)                           # User is logged in
dashboard(False)                          # User is not logged in


# Bsic multi_threading:
import threading                           # Import threading module

def task():                                # Create a function for the thread
    print(f"Task is running")              # Print message from the thread
t = threading.Thread(target=task)          # Create a thread
t.start()                                  # Start the thread
t.join()                                   # Wait for the thread to finish
print(f"Main program finished")            # Print after thread finishes

# Two threads:
import threading                           # Import threading module

def task1():                               # Create first task
    print(f"Task 1 is running")            # Print message for task 1

def task2():                               # Create second task
    print(f"Task 2 is running")            # Print message for task 2
t1 = threading.Thread(target=task1)        # Create thread 1
t2 = threading.Thread(target=task2)        # Create thread 2
t1.start()                                 # Start thread 1
t2.start()                                 # Start thread 2
t1.join()                                  # Wait for thread 1
t2.join()                                  # Wait for thread 2
print(f"All tasks completed")              # Print after both finish

# Two thread with loop:
import threading                           # Import threading module
def greet(name):                           # Create function with an argument
    print(f"Hello {name}")                 # Print the name
t = threading.Thread(                      # Create a thread
    target=greet,                          # Give greet function to thread
    args=("Amna",)                         # Pass Amna as argument
)
t.start()                                  # Start the thread
t.join()                                   # Wait for the thread to finish
print(f"Done")                             # Print after thread finishes


# Thread with sleep:
import threading                           # Import threading
import time                                # Import time for sleep()
def task1():                               # Create first task
    print(f"Task 1 started")               # Print when Task 1 starts
    time.sleep(1)                          # Wait for 1 second
    print(f"Task 1 finished")              # Print when Task 1 finishes

def task2():                               # Create second task
    print(f"Task 2 started")               # Print when Task 2 starts
    time.sleep(1)                          # Wait for 1 second
    print(f"Task 2 finished")              # Print when Task 2 finishes

t1 = threading.Thread(target=task1)        # Create thread 1
t2 = threading.Thread(target=task2)        # Create thread 2
t1.start()                                 # Start thread 1
t2.start()                                 # Start thread 2
t1.join()                                  # Wait for thread 1
t2.join()                                  # Wait for thread 2
print(f"All tasks completed")              # Print after both finish
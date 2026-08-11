
# Generator function
def my_generator():

    yield 1          # Return 1 and pause the function
    yield 2          # Return 2 and pause again
    yield 3          # Return 3 and then finish

# Get values one by one from the generator
for value in my_generator():            # Get one value at a time
    print(f"Value: {value}")            # Print the current value using f-string


# Generator function
def count():

    for i in range(1, 6):               # Loop from 1 to 5
        yield i                         # Return one value and pause the function

# Print values
for num in count():                     # Get values one by one
    print(f"Number: {num}")             # Print each value using f-string


# Generator function
# Next function()
def simple_gen():

    yield "Amna"        # Return "Amna" and pause the function
    yield "Yashfa"      # Return "Yashfa" and pause again
    yield "Nida"        # Return "Nida" and then finish

# Create generator object
gen = simple_gen()

# Print values one by one
print(f"First Name: {next(gen)}")       # Print first value
print(f"Second Name: {next(gen)}")      # Print second value
print(f"Third Name: {next(gen)}")       # Print third value


#  Fibonacci sequence Generator 
def fibonacci(n):                     # Define a generator function to generate Fibonacci numbers

    a = 0                             # First Fibonacci number
    b = 1                             # Second Fibonacci number

    for i in range(n):                # Repeat n times
        yield a                       # Return the current Fibonacci number and pause
        a, b = b, a + b               # Update the values for the next Fibonacci number

# Print Fibonacci numbers
for num in fibonacci(7):              # Get 7 Fibonacci numbers one by one
    print(f"Fibonacci Number: {num}") # Print each Fibonacci number 



# Create a generator expression(sqaures of numbers)
squares = (x * x for x in range(1, 6))   # Generate square of numbers from 1 to 5

# Print values one by one
for value in squares:                    # Get one value at a time
    print(f"Square: {value}")            # Print the current square


# Create a generator expression(Even numbers)
even = (x for x in range(1, 11) if x % 2 == 0)   # Generate even numbers from 1 to 10

# Print values
for num in even:                                 # Get one value at a time
    print(f"Even Number: {num}")                 # Print the current even number



# Send method( send a value to the generator):
def message_generator():

    while True:                             # Keep the generator running
        message = yield                     # Wait to receive a value
        print(f"Message: {message}")        # Print the received value using an f-string

# Create a generator object
gen = message_generator()                   # Call the generator function

next(gen)                                   # Start (prime) the generator

gen.send("Amna")                            # Send the first value
gen.send("Python")                          # Send the second value



# Close Method(stops the generator):
def my_gen():

    try:                               # Start a try block
        yield 1                        # Return 1 and pause the function
        yield 2                        # Return 2 and pause again
        yield 3                        # Return 3 and then finish

    finally:                           # Runs when the generator is closed
        print("Generator closed")      # Print a message when the generator closes

# Create a generator object
gen = my_gen()                         # Call the generator function

# Print the first value
print(f"First Value: {next(gen)}")     # Get and print the first value

# Close the generator
gen.close()                            # Stop the generator and run the finally block
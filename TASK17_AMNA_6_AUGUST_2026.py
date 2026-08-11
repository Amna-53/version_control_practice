# ITERATORS IN PYTHON:
print(f" ITERATORS IN PYTHON :")
print(iter("aa"))        # Create an iterator for the string "aa" and print its iterator object

print(iter([1, 2, 3]))   # Create an iterator for the list [1, 2, 3] and print its iterator object

print(iter((1, 2, 3)))   # Create an iterator for the tuple (1, 2, 3) and print its iterator object

print(iter({}))          # Create an iterator for the empty dictionary {} and print its iterator object


# ITERATORS WITH TRY AND EXCEPT:
print(f" Error Handling in Iterators")
it = iter([1,2,3, 4, 5])
print (next(it))
while True:
   try:
      no = next(it)
      print (no)
   except StopIteration:
      break



# CUSTOM ITERATORS:
#ITERATORS FOR ODD NUMBERS:
print(f"Iterators for odd numbers:")
class Oddnumbers:                      # Define a custom iterator class

    def __init__(self, end_range):     # Constructor to initialize variables
        self.start = -1                # Start from -1 so first odd number becomes 1
        self.end = end_range           # Store the ending range

    def __iter__(self):                # Return the iterator object
        return self

    def __next__(self):                # Return the next odd number
        if self.start < self.end - 1:  # Check if next odd number is within the range
            self.start += 2            # Move to the next odd number
            return self.start          # Return the current odd number
        else:
            raise StopIteration        # Stop iteration when the limit is reached

countiter = Oddnumbers(10)            # Create an iterator object with range 10

while True:                           # Keep looping until iteration ends
    try:
        no = next(countiter)          # Get the next odd number
        print(no)                     # Display the odd number
    except StopIteration:             # Catch the exception when no more values exist
        break                         # Exit the loop


# ITERATORS FOR EVEN NUMBERS:
# Create a class for generating even numbers
print(f"Iterators for even numbers:")
class EvenNumbers:

    # Constructor function runs when object is created
    def __init__(self, limit):
        self.number = 0          # Starting value of even numbers
        self.limit = limit       # Store the maximum limit

    # This method returns the iterator object
    def __iter__(self):
        return self              # Return the current object as iterator

    # This method returns the next value from iterator
    def __next__(self):

        # Check if current number is less than or equal to limit
        if self.number <= self.limit:

            even = self.number   # Store current even number

            self.number += 2     # Increase number by 2 for next even number

            return even         # Return the current even number

        # When limit is reached, stop the iteration
        raise StopIteration
    
# Create an object of EvenNumbers class with limit 10
even = EvenNumbers(10)
# Loop through iterator and print each even number
for value in even:
    print(value)                # Prints 0, 2, 4, 6, 8, 10


# ITERATORS WITH FOR LOOP:
# Create a list of fruits
print(f" Iterators with for loop:")
fruits = ["Apple", "Banana", "Mango"]

# Convert the list into an iterator
fruit_iterator = iter(fruits)
# Loop through the iterator one item at a time
for fruit in fruit_iterator:
    print(fruit)      # Prints "Apple", then "Banana", then "Mango"


# MANUAL ITERATION USING NEXT():
# Create a string
print(f" Iteraors using next:")
text = "Python"
# Convert the string into an iterator
text_iterator = iter(text)

print(next(text_iterator))      # next() returns 'P'
print(next(text_iterator))      # next() returns 'y'
print(next(text_iterator))      # next() returns 't'
print(next(text_iterator))      # next() returns 'h'
print(next(text_iterator))      # next() returns 'o'
print(next(text_iterator))      # next() returns 'n'

# If you call next() again, it will raise StopIteration
# print(next(text_iterator))    # No characters left



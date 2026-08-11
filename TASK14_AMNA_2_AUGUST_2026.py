# Function to print countdown using recursion
def countdown(n):                           # Define a recursive function
    if n <= 0:                              # Base case: when n becomes 0 or less, stop recursion
        print("done")                       # Print done after countdown finishes

    else:                                   # If n is greater than 0
        print(n)                            # Print the current number

        countdown(n - 1)                    # Call the function again with n decreased by 1

print("Countdown Output:")                  # Print heading to identify this program's output
countdown(5)                                # Call the function with starting value 5                       # Call the function with starting value 5

#To find the factorial of a number:
def factorial(n):
    if n == 0 or n == 1:    # base case where the recursion will stop 
        return 1

    return n * factorial(n - 1)     # this will return the factorial of the number by multiplying the number with the factorial of the number minus 1
print("factorial of 8 is :")
print(factorial(8))          # display the  total result of the factorial of 8

# Function to find Fibonacci numbers
def fibonacci(n):
    if n == 0:        # condtion to check if number is zero return it 
        return 0       # fabonacci of 0 is 0

    if n == 1:      # Condition to check if number is 1 simply return 1
        return 1     # fabonacci of 1 is 1

    return fibonacci(n - 1) + fibonacci(n - 2)  # add the two previous numbers to get the next number 
print("Fibonacci Output:")  
for i in range(6):           # loop that will run till 6 and will print the fibonacci of each number from 0 to 5
    print(fibonacci(i))      # print the numbers 


# Function to find sum of natural numbers:
def sum_numbers(n):                     # Define a recursive function
    if n == 1:                          # Base case: stop when n becomes 1
        return 1                        # Return 1

    return n + sum_numbers(n - 1)       # Add current number to the sum of previous numbers
print("sum of numbers:")
print(sum_numbers(5))                   # Call the function with 5 and print the result


# Power of a number :
def power(x, n):                        # Define a recursive function

    if n == 0:                          # Base case: any number raised to power 0 is 1
        return 1                        # Return 1

    return x * power(x, n - 1)          # Multiply x by the result of x^(n-1)
print("power of number:")
print(power(2, 4))                      # Call the function with x = 2 and n = 4, then print the result

# Function to reverse a string
def reverse_string(text):                   # Define a recursive function

    if text == "":                          # Base case: if the string is empty, stop recursion
        return ""                           # Return an empty string

    return reverse_string(text[1:]) + text[0]   # Reverse the remaining string and add the first character at the end
print("Reverse string is :")
print(reverse_string("Python"))             # Call the function with "Python" and print the reversed string

# Recursive function to check if a number is even
def is_even(n):                           # Define a recursive function

    if n == 0:                            # Base case: 0 is an even number
        return True                       # Return True

    if n == 1:                            # Base case: 1 is an odd number
        return False                      # Return False

    return is_even(n - 2)                 # Subtract 2 and check again
print("Even number check output:")
print(is_even(8))                         # Call the function with 8 and print the result



# Function to find the maximum value recursively:
def find_max(lst, n):                         # Define a recursive function

    if n == 1:                                # Base case: if only one element is left
        return lst[0]                         # Return the first element

    maximum = find_max(lst, n - 1)            # Find the maximum in the first (n-1) elements

    if lst[n - 1] > maximum:                  # Check if the last element is greater
        return lst[n - 1]                     # Return the last element if it is larger
    else:                                     # Otherwise
        return maximum                        # Return the previous maximum

numbers = [5, 12, 8, 20, 7]                   # Create a list of numbers
print ("Maximum value is :")
print(find_max(numbers, len(numbers)))        # Find and print the maximum value


# Recursive binary search function
def binary_search(arr, low, high, target):       # Define a recursive function for binary search

    if low > high:                               # Base case: if search range becomes empty
        return -1                                # Return -1 means target is not found

    mid = (low + high) // 2                      # Find the middle index of the search range

    if arr[mid] == target:                       # Check if the middle element is equal to target
        return mid                              # Return the index if target is found

    elif target < arr[mid]:                      # Check if target is smaller than middle element
        return binary_search(arr, low, mid - 1, target)   # Search in the left half

    else:                                        # If target is greater than middle element
        return binary_search(arr, mid + 1, high, target)  # Search in the right half

numbers = [2, 4, 6, 8, 10, 12]                  # Create a sorted list of numbers
print("Binary search Output: ")
print(binary_search(numbers, 0, len(numbers)-1, 8))  # Call function and print index of target


# Function to find GCD using recursion
def gcd(a, b):                              # Define a recursive function to find GCD

    if b == 0:                              # Base case: when b becomes 0, stop recursion
        return a                            # Return a as the GCD

    return gcd(b, a % b)                    # Call function again with b and remainder of a divided by b
print("Gcd output: ")
print(gcd(24, 18))                          # Call the function with 24 and 18 and print the result


# Function to check palindrome
def palindrome(word):                         # Define a recursive function to check palindrome

    if len(word) <= 1:                        # Base case: if word has 0 or 1 character, it is palindrome
        return True                           # Return True

    if word[0] != word[-1]:                   # Check if first and last characters are not same
        return False                          # Return False because word is not palindrome

    return palindrome(word[1:-1])             # Remove first and last character and check the remaining word

word = "madam"                                # Create a word to check
print("palindrome Output: ")
print(palindrome(word))                       # Call the function and print the result
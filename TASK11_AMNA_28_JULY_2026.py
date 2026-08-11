# Binary Search 
# Iterative implementation of binary serach algorithm 
# Binary Search Function
def binarySearch(array, x, low, high):   # Function to search x in a sorted array

    # Keep searching until low becomes greater than high
    while low <= high:

        mid = low + (high - low) // 2    # Find the middle index of the current search area

        if x == array[mid]:              # Check if the middle element is the target
            return mid                   # Return the index if the element is found

        elif x > array[mid]:             # Check if x is greater than the middle element
            low = mid + 1                # Search in the right half by moving low

        else:                            # If x is smaller than the middle element
            high = mid - 1               # Search in the left half by moving high

    return -1                            # Return -1 if the element is not found

# Sorted array for Binary Search
array = [3, 4, 5, 6, 7, 8, 9]

# Element we want to search
x = 4

# Call the binarySearch function
# low = 0 (first index)
# high = len(array)-1 = 6 (last index)
result = binarySearch(array, x, 0, len(array) - 1)

# Check whether the element was found
if result != -1:
    print("Element is present at index", result)   # Print the index where the element is found
else:
    print("Not found")                             # Print if the element does not exist


#Recursive implementation of binary search algorithm
# Recursive Binary Search Function
def binarySearch(array, x, low, high):      # Function to search x using recursion
    if high >= low:                         # Continue searching if low is less than or equal to high

        mid = low + (high - low) // 2       # Find the middle index

        if x == array[mid]:                 # Check if the middle element is the target
            return mid                      # Return the index if found

        elif x > array[mid]:                # Check if x is greater than the middle element
            return binarySearch(array, x, mid + 1, high)
                                            # Search the right half by calling the function again
        else:                               # If x is smaller than the middle element
            return binarySearch(array, x, low, mid - 1)
                                            # Search the left half by calling the function again

    else:                                   # If low becomes greater than high
        return -1                           # Return -1 because the element is not found

# Sorted array
array = [3, 4, 5, 6, 7, 8, 9]
# Element to search
x = 4
# Call the recursive binary search function
# low = 0 (first index)
# high = len(array)-1 = 6 (last index)
result = binarySearch(array, x, 0, len(array) - 1)

# Check whether the element is found
if result != -1:
    print("Element is present at index", result)   # Print the index where the element is found
else:
    print("Not found")                             # Print if the element is not found
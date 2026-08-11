# Bubble Sort Algorithm(ascending order)
def bubble_sort(array, size):           # Function to sort the array
    for i in range(size):               # Outer loop for each pass
        swaps = 0                       # Variable to check if any swap occurs
        for j in range(0, size - i - 1):  # Inner loop for comparing adjacent elements
             
            if array[j] > array[j + 1]:  # If left element is greater than right element
                temp = array[j]          # Store current element in a temporary variable
                array[j] = array[j + 1]  # Move the next element to the current position
                array[j + 1] = temp      # Place the stored element in the next position

                swaps = 1                # A swap has occurred

        if swaps == 0:                  # If no swaps happened
            break                       # Stop because the array is already sorted
arr = [67, 44, 82, 17, 20]              # Create a list of numbers
n = len(arr)                            # Find the total number of elements

print("Array before Sorting:")          # Display message
print(arr)                              # Print original array

bubble_sort(arr, n)                     # Call the Bubble Sort function

print("Array after Sorting:")           # Display sorted array 
print(arr)                              # Print  the sorted array

# Bubble Sort Algorithm (Descending Order)
def bubble_sort_desc(arr):                 # Function to sort the array in descending order
    n = len(arr)                           # Find the number of elements in the array
    for i in range(n):                     # Outer loop for each pass
        for j in range(n - i - 1):         # Inner loop for comparing adjacent elements
            if arr[j] < arr[j + 1]:        # If the left element is smaller than the right element
                # Swap the two elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22]                 # Create a list of numbers

bubble_sort_desc(arr)                      # Call the function to sort the list
print(arr)                                 # Print the sorted list
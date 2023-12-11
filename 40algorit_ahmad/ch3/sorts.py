def bubbleSort(arr):
    # Index i is the position where the element will bubble
    # to (minus 1 for in order to swap in the final position)
    for i in range(len(arr)-1, 0, -1):
        # Index j is to iterate through elements up until
        # the bubble position i
        # Move elements right, but move the endpoint left
        for j in range(i):
            if arr[j] > arr[j+1]:
                # In place sort
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionSort(arr):
    # Index i is the element that we want to insert to the left
    # so i sweeps right to left
    for i in range(1, len(arr)):
        # Extract element at index i
        current_element = arr[i]

        # Define start point for swaps
        j = i-1

        # Loop through indices less that i to find
        # insertion point
        while (arr[j] > current_element) and (j >= 0):
            # Move to the  right (to sort element to the left)
            arr[j+1] = arr[j]

            j -= 1

        # Slot element at i into spot j
        arr[j+1] = current_element

def mergeSort(arr):
    # Merge sort wants a single element
    if len(arr) > 1:
        # Find midpoint
        midpoint = len(arr)//2

        # Split into left and right
        left  = arr[:midpoint]
        right = arr[midpoint:]

        # Recursive call for merge sorting the left and right
        mergeSort(left)
        mergeSort(right)

        # Actual sorting occurs here
        # Placeholder indices
        a = b = c = 0
        
        # a and b can be up to the length of the left/right lists
        while a < len(left) and b < len(right):
            # Start at the beginning of each list and
            # pull the elements out in incremental order
            if left[a] < right[b]:
                arr[c] = left[a]
                a = a + 1
            else:
                arr[c] = right[b]
                b = b + 1

            # Increment the length of the overall list
            c = c + 1

        # Loop through the remnants of the left and right hand sides
        # for unequal lists. If the previous loop has been executed,
        # then any remnant of the left or right lists will all be greater
        # than the elements of the other list
        # Left is longer than right, additional loop for the left
        while a < len(left):
            arr[c] = left[a]
            a = a + 1
            c = c + 1
        
        # Right is longer than left, additional loop for the right
        while b < len(right):
            arr[c] = right[b]
            b = b + 1
            c = c + 1

def shellSort(arr):
    # Define the distance between points to compare
    # Start with the element an increment of half the list away
    distance = len(arr)//2

    while distance > 0:
        # Loop through elements in the back portion of the list
        for i in range(distance, len(arr)):
            # Pull element at index i out
            tmp = arr[i]

            # Create placeholder index for the first portion of the
            # list
            j = i

            # Sort the sub list of elements j and every distance index
            # j >= distance so j doesn't cross into another portion of the
            # list
            # arr[j - distance] > tmp for swapping elements
            while j >= distance and arr[j - distance] > tmp:
                # Swap elements
                arr[j] = arr[j - distance]

                # Take step size of size distance
                j -= distance

            # Finally put the tmp element back
            arr[j] = tmp
        
        # Cut the distance in half
        distance = distance//2

def selectionSort(arr):
    # Fill from right to left
    # Index i is the location to put the ith largest
    # value
    for i in range(len(arr)-1, 0, -1):
        # Keep track of where the largest value will go
        position_for_max_value = 0

        # j is the element being moved
        # i goes to length of input - 1, so i + 1
        # puts us to the endpoint
        for j in range(1, i + 1):
            # If the element at the jth position is 
            # bigger, than we want that to be noted as the
            # position for the maximum value
            if arr[j] > arr[position_for_max_value]:
                position_for_max_value = j

        # Perform a single swap
        arr[i], arr[position_for_max_value] = arr[position_for_max_value], arr[i]
            

def quickSort(arr):
    # Get length of input list
    n = len(arr)
    
    # Terminate if n <= 1
    if n <= 1:
        return arr
    
    # Sort small chunks using a different sort to remove 
    # recursive calls. Define some arbitrary length to use this for
    if n <= 15:
        mergeSort(arr) 
        return arr
    
    # Choose first element as the pivot
    pivot = arr[0] 
    
    # Separate vector into three chunks
    lhs = [x for x in arr if x < pivot]
    rhs = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]
    
    # Recursively sort elements less than pivot (left hand side) and 
    # elements greater than the pivot (right hand side)
    return quickSort(lhs) + mid + quickSort(rhs)


if __name__ == '__main__':
    import numpy as np
    import random
    import time

    test = [round(np.random.rand(), 3) for _ in range(1000)]
    output = quickSort(test)
    print(output)
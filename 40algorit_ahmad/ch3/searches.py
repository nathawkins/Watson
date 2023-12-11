from sorts import bubbleSort

def linearSearch(arr, item):
    for val in arr:
        if val == item:
            return True
    return False

def binarySearch(arr, item):
    # Requires sorted data
    bubbleSort(arr)

    # Define boundaries of search that will incrementally change
    first_index = 0
    last_index  = len(arr)-1
    found       = False
    while first_index <= last_index and not found:
        # Identify the midpoint of current segement
        midpoint = (first_index + last_index)//2

        # Determine which side of the tree to search
        if arr[midpoint] == item:
            found = True
        
        # If not, identify which side of the tree to search
        else:
            if item < arr[midpoint]: # On left hand side
                last_index = midpoint - 1
            else: # On right hand side
                first_index = midpoint + 1
    
    return found

def interpolationSearch(arr, item):
    # Requires sorted array
    bubbleSort(arr)

    # Define bounds of search which will change
    starting_index = 0
    ending_index   = len(arr) - 1

    while starting_index <= ending_index and item >= arr[starting_index] and item <= arr[ending_index]:
        # Calculate the midpoint
        # 1. Number of indices between start and end
        term_1 = float(ending_index - starting_index)

        # 2. Difference between values at that index
        term_2 = arr[ending_index] - arr[starting_index]

        # 3. Quotient of term 1 and 2
        term_3 = term_1/term_2

        # 4. Multiply by difference between target item and starting index
        term_4 = item - arr[starting_index]

        # 5. Product of term 3 and 4
        term_5 = int(term_3 * term_4)

        # 6. Add that to the syatyomg index to move it
        # Idea is to figure out the average number of indices
        # to cover range of values, then multiply that by how much
        # the target item is from our starting position
        midpoint = starting_index + term_5

        if arr[midpoint] == item:
            return True

                
        if arr[midpoint] < item:
            starting_index = midpoint + 1

    return False


if __name__ == '__main__':
    test = [12, 67, 3, 111, 1738, 9]
    print(interpolationSearch(test, 3))
    print(interpolationSearch(test, 9))
    print(interpolationSearch(test, 1))
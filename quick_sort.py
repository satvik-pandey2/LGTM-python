def quicksort(arr):
    # Base case: an empty list or a single element list is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (we can choose the first, last, or middle element)
    pivot = arr[len(arr) // 2]

    # Partition the list into three parts:
    # - Elements less than the pivot
    # - Elements equal to the pivot
    # - Elements greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively apply quicksort to the left and right partitions, and concatenate them
    return quicksort(left) + middle + quicksort(right)

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Track if any swaps happen; useful for optimization
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped, the list is already sorted
        if not swapped:
            break

    return arr

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)

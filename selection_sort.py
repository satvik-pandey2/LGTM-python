def selection_sort(arr):
    # Loop through the entire list
    for i in range(len(arr)):
        # Find the minimum element in the unsorted part of the list
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)

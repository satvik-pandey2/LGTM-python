def insertion_sort(arr):
    # Loop through each element in the list starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # The element we want to insert into the sorted part of the list
        j = i - 1  # Start comparing with the element before it

        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at its correct position
        arr[j + 1] = key

    return arr

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)

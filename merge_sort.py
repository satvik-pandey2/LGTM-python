def mergesort(arr):
    # Base case: if the list has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle index of the list
    mid = len(arr) // 2

    # Recursively split the list into two halves
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    
    # Merge the two sorted halves
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare elements of both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # If any elements are left in either half, append them
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = mergesort(arr)
print("Sorted array:", sorted_arr)

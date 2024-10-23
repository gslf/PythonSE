def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0...i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key at its correct position
        arr[j + 1] = key
    
    return arr

# Test
my_list = [64, 5, 25, 12, 22, 11, 90]
sorted_list = insertion_sort(my_list)
print("Sorted array:", sorted_list)

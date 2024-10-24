def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum element is the first unsorted element
        min_index = i
        for j in range(i + 1, n):
            # Find the minimum element in the remaining unsorted section
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted region
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
my_list = [12, 11, 13, 5, 6]
selection_sort(my_list)
print("Sorted array:", my_list)
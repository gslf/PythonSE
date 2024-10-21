def bubble_sort(arr):
    n = len(arr)

    # Loop through the entire list n times
    for i in range(n):
        swapped = False

        # Compare each pair of adjacent elements and move larger ones to the end
        for j in range(0, n - i - 1):

            # If the current element is larger than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no elements were swapped, the list is already sorted
        if not swapped:
            break
            
    return arr

# Test
my_list = [64, 5, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print("Sorted array:", sorted_list)
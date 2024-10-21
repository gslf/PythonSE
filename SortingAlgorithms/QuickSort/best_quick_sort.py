def quick_sort_in_place(arr, low, high):
    if low < high:
        # Partition the array and get the partition index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort the elements before and after partition
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Median-of-three to choose a pivot
    mid = (low + high) // 2
    pivot = median_of_three(arr, low, mid, high)
    
    # Partition the array around the pivot
    # moving all the smaller element to the left of the pivot.
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Replace the pivot in his new position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def median_of_three(arr, low, mid, high):
    # Sort the three elements and return the median as pivot
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    # Use the middle element as the pivot
    arr[mid], arr[high] = arr[high], arr[mid]
    return arr[high]

# Test
my_list = [64, 5, 25, 12, 22, 11, 90]
quick_sort_in_place(my_list, 0, len(my_list) - 1)
print("Sorted array:", my_list)

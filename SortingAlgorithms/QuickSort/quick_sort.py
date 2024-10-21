def quick_sort(arr):
    # Base case: a list of 1 or 0 elements is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (commonly the last element in the list)
    pivot = arr[len(arr) // 2]

    # Partitioning step: divide the list into three sublists
    left = [x for x in arr if x < pivot]   # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]   # Elements greater than pivot

    # Recursively apply quick_sort to both partitions
    return quick_sort(left) + middle + quick_sort(right)

# Test
my_list = [64, 5, 25, 12, 22, 11, 90]
sorted_list = quick_sort(my_list)
print("Sorted array:", sorted_list)
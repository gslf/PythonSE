def merge_sort(arr):
    # Base case: if the array has 1 or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index of the array to split it into two halves
    mid = len(arr) // 2

    # Recursively split and sort both halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    # Create an empty list to hold the merged result
    merged = []

    # Use two pointers to traverse both arrays
    i = 0  # Pointer for the left half
    j = 0  # Pointer for the right half

    # Compare elements from both halves and append the smaller one to the merged list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # If there are remaining elements in the left half, append them
    merged.extend(left[i:])

    # If there are remaining elements in the right half, append them
    merged.extend(right[j:])

    return merged

# Test
my_list = [64, 5, 25, 12, 22, 11, 90]
sorted_list = merge_sort(my_list)
print("Sorted array:", sorted_list)
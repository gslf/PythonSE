def merge_sort(arr, left, right):

    if left < right:
        # Find the middle index
        mid = (left + right) // 2

        # Recursively sort both halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Merge the two sorted halves
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    # Create temporary arrays to hold the two halves
    n1 = mid - left + 1
    n2 = right - mid

    # Copy data to temporary arrays left and right
    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]

    # Initial index of the two halves
    i = 0  # Initial index of left half
    j = 0  # Initial index of right half
    k = left  # Initial index of merged array

    # Merge the temporary arrays back into arr[left:right+1]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[] (if any)
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[] (if any)
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Test
my_list = [64, 5, 25, 12, 22, 11, 90]
merge_sort(my_list, 0, len(my_list)-1)
print("Sorted array:", my_list)
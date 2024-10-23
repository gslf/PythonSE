# The Merge Sort Algorithm in Python

Merge Sort is an efficient sorting algorithm that utilizes the divide-and-conquer technique. 
Below is a graphical representation of how it works:

![Merge Sort algorithm - visual representation](/SortingAlgorithms/MergeSort/res/merge_sort_visualization.png)

## How Merge Sort Works
- **Dividing the List**: Merge Sort begins by dividing the unsorted list into two approximately equal halves. This process is repeated recursively until each sublist contains a single element (since a list of one element is inherently sorted).
- **Recursive Merging the Sublists**: Once the base case of single-element lists is reached, the algorithm starts merging the sublists. During this merge process, it compares the smallest elements of the sublists and arranges them in sorted order. The merging continues recursively as the sorted sublists are combined back together into larger and larger lists. Eventually, the entire list is merged back into a fully sorted order.

## Implementation

This is the simplest python implementation of Merge Sort in python:

```python
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

```

This implementation is simple to understand, and it works, but can be improved.
1. **Avoiding unnecessary slicing:** Slicing creates a copy of the array, which can be inefficient in terms of both time and memory usage. We can avoid copying by passing indices to define the subarrays rather than slicing them.
2. ** Optimize memory usage during merging:** Instead of creating new lists for the merged array, we can optimize this by modifying the original array in-place during the merge step, which helps save memory.

```python
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
```

## QuickSort vs MergeSort
While QuickSort excels with average-case performance due to its in-place sorting, Merge Sort guarantees stability and consistent O(n log n) time complexity, making it more predictable for large datasets, albeit with higher memory usage.
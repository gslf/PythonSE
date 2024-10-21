# The Quick Sort Algorithm in Python

Quick Sort is a eddicient sorting algorithm that use the **divide-and-conquer** tactics. This is a graphical representation of how it works:

![Quick Sort algorithm - visual representation](/SortingAlgorithms/QuickSort/res/quick_sort_visualization.png)

## How Quick Sort Works
- **Choosing a Pivot:** Quick Sort begins by selecting a pivot element from the list. A common approach is to pick the middle element, but in practice, any element could serve as the pivot.
- **Partitioning:** The list is then divided into three parts:
    - Elements smaller than the pivot
    - Elements equal to the pivot
    - Elements larger than the pivot
- **Recursive Sorting:** After partitioning, Quick Sort is recursively applied to both the left and right sublists. This process continues until all sublists contain only one element, at which point the list is fully sorted.


This is a simple python implementation of Quick Sort Algorithm:

```python
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
```

This implementation is simple to understand, but can be improved by making two major changes:
- **In-place sorting**: The algorithm can be implemented to use less space, avoiding the creation of new lists for partitions. We can modify the original array "in-place" using pointers (indices) for the partitions.

- **Optimization of pivot selection**: The choice of the pivot can significantly affect performance. A common technique to improve pivot selection is the "median of three," which chooses the pivot by taking the median value of the first, middle, and last elements of the list. This helps ensure a more balanced partition by avoiding consistently poor pivot choices, especially in nearly sorted or highly skewed data.

Here is the more efficient implementation. It is a bit more complex to understand but faster, so it can also be used in production:
```python
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

```     

Quick Sort has a time complexity of O(n log n), which makes it one of the most popular sorting algorithms for practical use. However, in the worst case (e.g., when the pivot is always the largest or smallest element), Quick Sort can degrade to O(n²), though this is relatively rare in practice.
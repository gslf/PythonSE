# Tim Sort in Python

TimSort is a hybrid sorting algorithm that combines the best aspects of **Merge Sort** and **Insertion Sort**. Developed by Tim Peters in 2002, this algorithm is the default sorting technique used in Python's built-in sort() and Java's Arrays.sort() for non-primitive types. What makes TimSort particularly effective is its ability to adapt to the structure of **real-world data**, using existing order in datasets to optimize sorting performances.

TimSort operates by dividing the data into smaller segments called "runs," which are sequences of consecutive elements already sorted or sortable using [Insertion Sort](/SortingAlgorithms/InsertionSort/README.md). These runs are then merged using a process inspired by [Merge Sort](/SortingAlgorithms/MergeSort/README.md).

![Tim Sort algorithm - visual representation](/SortingAlgorithms/TimSort/res/tim_sort_visualization.png)

## Implementation
```python
from typing import List

MIN_RUN = 33

def insertion_sort(array: List[int], left: int, right: int) -> None:
    """Sort a section of the array using Insertion Sort."""
    for i in range(left + 1, right + 1):
        key = array[i]
        j = i - 1
        while j >= left and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def merge(array: List[int], left: int, mid: int, right: int) -> None:
    """Merge two sorted subarrays into one sorted segment."""
    left_part = array[left:mid + 1]
    right_part = array[mid + 1:right + 1]

    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        array[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        array[k] = right_part[j]
        j += 1
        k += 1

def tim_sort(array: List[int]) -> None:
    """Sort the array using TimSort algorithm."""
    n = len(array)

    # Divide the array into runs of size MIN_RUN and sort each run
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(array, start, end)

    # Merge runs iteratively
    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(array, left, mid, right)
        size *= 2

# Example usage
if __name__ == "__main__":
    arr = [5, 2, 3, 8, 7, 6, 1, 4]
    tim_sort(arr)
    print(arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
```

In this basic implementation of TimSort, several optimizations can be introduced to improve its efficiency and robustness:

- **Dynamic Run Identification:** Automatically detect runs in both ascending and descending order rather than relying on fixed-sized segments.
- **Adaptive Insertion Sort Threshold:** Use a variable MIN_RUN size based on the size of the input array for better adaptability.
- **Galloping Mode:** Integrate a galloping mode for faster merging when one of the subarrays is significantly smaller than the other.
- **Run Stack Management:** Maintain a stack of runs to enforce merging rules that prevent creating deeply nested merge operations.
- **In-Place Merging:** Optimize the merge function to reduce auxiliary space usage during merging.
- **Parallel Processing:** Explore multi-threading or parallel processing for independent runs, particularly in large datasets.
- **Special Case Handling:** Optimize for edge cases like already sorted arrays, reverse-sorted arrays, and arrays with many duplicate elements for O(n) performance in such cases.
- **Type Flexibility:** Extend support for custom comparator functions to handle complex data types or domain-specific sorting logic.

## Performance Evaluation

TimSort is highly efficient for real-world datasets with partially ordered data due to its adaptive nature. 

Time Complexity:
- Best Case: O(n) (when the array is already sorted)
- Average Case: O(n log n)
- Worst Case: O(n log n)

Space Complexity:
- O(n) (due to auxiliary space used during merging)
# The Selection Sort Algorithm in Python

Selection Sort is an algorithm that doesn’t attempt to predict the future (as mergesort does by pre-dividing the list) or make assumptions (like quicksort with its pivots). Instead, it focuses on what is certain—identifying the smallest element—and advances methodically, one step at a time. In software engineering, the simplest, most deliberate approach is often the most enlightening, especially when mastering the fundamentals.

## How it works
Selection sort operates by partitioning the input list into a sorted and an unsorted region. Initially, the sorted region is empty, and the unsorted region contains the entire list. The algorithm iteratively selects the smallest element from the unsorted region and swaps it with the leftmost unsorted element, effectively expanding the sorted region and shrinking the unsorted one.

Think of selection sort as tidying up a cluttered shelf of books. Imagine each book has a different height, and you want to arrange them from shortest to tallest. You look at the whole row, select the shortest book, and place it at the leftmost empty position on the shelf. You repeat the process: look at the unsorted section, grab the next shortest book, and position it correctly. By the time you reach the end of the shelf, all books are neatly arranged.

![Selection Sort algorithm - visual representation](/SortingAlgorithms/SelectionSort/res/selection_sort_visualization.png)

## Implementation
```python
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
```

Selection sort is a prime example of the trade-offs between simplicity and efficiency. Conceptually, it's straightforward: find the smallest item, place it in order, and repeat. There are no complex recursive structures, no splitting or merging of data—just systematic selection and swapping.

However, this simplicity comes with a cost: O(n^2) time complexity for both average and worst-case scenarios. The algorithm's performance degrades rapidly as the input size grows, and it lacks the adaptive qualities of algorithms like insertion sort or the sophisticated partitioning strategies of quicksort. Yet, there's an elegance to selection sort's deterministic, step-by-step nature. It is predictable, reliable, and requires only O(1) additional memory, an important trait in resource-constrained environments.
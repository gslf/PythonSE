# The Bubble Sort Algorithm in Python

Bubble Sort is a sorting algorithm that operates with a fundamentally **human approach** to problem-solving: making pairwise comparisons and gradually improving the situation by addressing small errors at each step. The algorithm repeatedly steps through a list, compares adjacent elements, and swaps them if they are in the wrong order. This continues until the entire list is sorted.

Here is a visual representation of how the Bubble Sort algorithm works, step-by-step:

![Bubble Sort algorithm - visual representation](/SortingAlgorithms/BubbleSort/res/bubble_sort_visualization.png)

## Implementation
This is the python implementation of Bubble Sort Algorithm

```python
def bubble_sort(arr):
    n = len(arr)

    # For each element in the list
    for i in range(n):
        swapped = False

        # Check all the other elements to find the largest one
        for j in range(0, n - i - 1):

            # If you find a bigger one, swap it with the current
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no elements were swapped, the list is already sorted
        if not swapped:
            break

    return arr

# Test
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print("Sorted array:", sorted_list)
```

This algorithm is very simple, but this simplicity comes at a cost: with a time complexity of O(n²) in the average and worst cases, Bubble Sort performs poorly on large datasets. One of the more obvious criticisms of Bubble Sort is its redundancy. The algorithm continues making passes over the list even when the list is already sorted, wasting time and computational effort. 
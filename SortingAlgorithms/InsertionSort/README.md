# The Insertion Sort Algorithm in Python

Insertion Sort is a simple algorithm that works very well with small amounts of data. With each step, the algorithm picks the next element and places it in its correct position among the previously sorted elements. This makes it intuitive and efficient for small datasets, but less optimal for larger ones.

Here’s a visual analogy: think of sorting playing cards in your hand. You pick up one card at a time, and then you place it into the correct position relative to the other cards in your hand, shifting the others if necessary.

## How it works
Insertion Sort iterates over the list, taking one element at a time and inserting it into its correct position in the sorted part of the list. This process continues until all elements are sorted. Each pass involves shifting elements of the sorted section of the list to create space for the new element.

Here is a visual representation of how the Insertion Sort algorithm works, step-by-step:

![Insertion Sort algorithm - visual representation](/SortingAlgorithms/InsertionSort/res/insertion_sort_visualization.png)

## Implementation
Here’s the Python implementation of the Insertion Sort algorithm:

```python
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0...i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key at its correct position
        arr[j + 1] = key
    
    return arr

# Test
my_list = [12, 11, 13, 5, 6]
sorted_list = insertion_sort(my_list)
print("Sorted array:", sorted_list)
```

The algorithm starts by assuming that the first element is already sorted. It then picks the next element (key) and compares it with the elements before it. If the previous element is larger than the key, it shifts that element to the right. This process continues until the key is placed in its correct position.

While Insertion Sort is simple and effective for small lists, it has a time complexity of O(n²) in the average and worst cases. This quadratic complexity comes from the nested loops—one for iterating over the list and one for shifting elements. However, in the best-case scenario, where the list is already sorted, the time complexity is O(n), making it more efficient than many other O(n²) sorting algorithms in certain situations.

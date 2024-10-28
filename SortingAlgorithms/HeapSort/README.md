# The Heap Sort algorithm in Python

Heap Sort is an algorithm that sorts an array by building a heap structure, specifically a Max Heap, and repeatedly extracting the maximum element, ensuring efficient time complexity and memory stability. A Max Heap is a binary tree where each parent node is greater than or equal to its children, with the maximum value at the root.

Imagine you are organizing a playlist of songs for a party, and you want the most popular, energetic tracks to play first. You start by ranking all the songs based on their popularity and energy level (Heap Construction). Once you have the most energetic song, you play it (Extracting the Maximum), and then you re-evaluate the rest to ensure the next best song is played (Reforming the Heap). You continue this until you've played all the songs in order, maintaining the highest energy throughout.

Heap Sort embodies several principles of software engineering, including hierarchical control, space-time efficiency, and a certain structural minimalism. The construction of a heap is the epitome of a "divide and conquer" approach with a twist: it does not excessively fragment, but rather organizes to maintain global control.


## How it work
The algorithm can be broken down into the following key steps:

1. Heap Construction: First, the array to be sorted is transformed into a Max Heap, a structure where each node is greater than (or equal to) its children. This is achieved by calling the "heapify" function on all nodes starting from the middle of the array up to the root.
2. Extracting the Maximum: Once the Max Heap is built, the maximum element (located at the root) is swapped with the last element of the array. This positions the maximum at the end of the array, progressively sorting the elements.
3. Reform the Heap: After swapping the root with the last element, the algorithm virtually removes the maximum (reducing the heap size) and calls "heapify" again to reform a Max Heap with the remaining elements.
4. Repetition: This process of extraction and heap reformation is repeated until the entire array is sorted.

![heap Sort algorithm - visual representation](/SortingAlgorithms/HeapSort/res/heap_sort_visualization.png)

## Implementation
Let's look at an implementation of Heap Sort in Python

```python
def heapify(arr, n, i):
    # Find the largest among current node, left child, and right child
    largest = i  # Initially assume the current node is the largest
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If the left child is larger than the current node
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right child is larger than the current (or left if already changed)
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Check if the largest is not the current node, swap and continue heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Continue heapifying the affected sub-tree


def heap_sort(arr):
    n = len(arr)

    # Build a Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move the root to the end
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        # Reform the Max Heap on the reduced array
        heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)
```
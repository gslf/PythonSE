# The Counting Sort algorithm in Python

Counting Sort is a non-comparison-based algorithm that works exceptionally well for sorting integers or elements from a limited range. Instead of comparing individual elements, it builds a count of occurrences of each element and uses this count to determine the position of each element in the final sorted array. This means that Counting Sort is very efficient when the range of input values is not vastly greater than the number of items to be sorted.

Imagine you are sorting a bag of colored marbles where each color represents a distinct number. Instead of comparing the marbles, you first separate them by color, counting how many of each color exist. Next, you line them up according to the counts, with marbles of the same color placed consecutively.

## How it work

1. Count Occurrences: Start by creating a frequency array. For each value in the array, increment its count in a separate count array.
2. Cumulative Count: Transform this count array into a cumulative count array. This will give you the positions where each element should be placed in the sorted array.
3. Build the Sorted Output: Finally, use this cumulative information to place each element in its correct position, iterating from right to left to preserve stability (order of equivalent elements).

![Counting Sort algorithm - visual representation](/SortingAlgorithms/CountingSort/res/counting_sort_visualization.png)

## Implementation
Here is an implementation of the vucket sort algorithm in python:

```python
```

Unlike other general-purpose sorting algorithms, Counting Sort's complexity is linear with respect to the number of items plus the range of input, making it , where  is the number of elements to be sorted, and  is the range of input. The critical advantage here is the avoidance of element comparison, which is a defining feature of most other common sorting methods.
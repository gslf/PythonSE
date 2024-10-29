# The Radix Sort algorithm in Python

Radix Sort is a non-comparative sorting algorithm that processes data by sorting it digit by digit, starting from the least significant digit to the most significant digit (LSD) or the opposite (MSD). It's fundamentally different from comparison-based sorts like Quicksort or Mergesort, as it leverages properties of the keys (usually numbers) themselves rather than comparing pairs of elements. It's particularly efficient for numbers or fixed-length strings, and it can achieve linear time complexity in certain conditions, making it an optimal choice for specialized datasets.

Radix Sort represents a beautifully deterministic approach to problem-solving. Instead of tackling the entire problem (sorting) at once by comparing every possible pairing, Radix Sort approaches it incrementally, solving it step-by-step by considering local properties (each individual digit). It takes inspiration from reductionism in philosophy—breaking down a problem into simpler, solvable parts, and building up the solution through iteration and synthesis.

![Radix Sort Algorithm - visual representation](/SortingAlgorithms/RadixSort/res/radix_sort_visualization.png)


## How it work
Radix Sort works by:

1. Partitioning the elements into buckets, based on individual digits or characters.
2. Processing these buckets one digit at a time, re-sorting the entire list according to each level of significance, starting with the least significant.
3. Repeating the process for every digit, until all elements are sorted.

The important takeaway is that Radix Sort doesn’t depend on pairwise comparisons but instead uses the inherent structure of the numbers to sort efficiently. This is what makes it particularly well-suited for inputs with uniformly distributed values and a fixed number of digits.

## Implementation
This is a Python implementation of Radix Sort, written with clarity and adherence to Pythonic best practices.

```python
from typing import List

def counting_sort(arr: List[int], exp: int) -> None:
    """
    A utility function to perform counting sort on the array based on the digit represented by 'exp'.
    """
    n = len(arr)
    output = [0] * n  # Output array to hold sorted values for this digit
    count = [0] * 10  # Count array for each digit (0-9)

    # Count occurrences of each digit at 'exp' place
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Transform count to represent the position of each digit in output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array by placing elements in the correct position
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy sorted values back to original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr: List[int]) -> None:
    """
    Main function to sort an array using Radix Sort algorithm.
    """
    if not arr:
        return

    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    
    # Iterate over each digit's place (exp: 1, 10, 100, ...)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage
arr = [64, 5, 25, 12, 22, 11, 90, 329, 457, 657, 839, 436, 720, 355]
radix_sort(arr)
print("Sorted array:", arr)
```

Radix Sort may not always be the go-to algorithm due to its space overhead and the requirement of integer-like data structures, but it's a powerful tool when used in the right context. 
# Shell sort in Python

Shell Sort is a comparison-based sorting algorithm that is an improvement over the simple insertion sort algorithm. Developed by **Donald Shell** in 1959, Shell Sort gets its name from the way it "breaks" the original list into smaller sublists, which are then sorted using insertion sort. This unique approach makes Shell Sort more efficient than traditional sorting algorithms, especially for larger data sets.

The main idea behind Shell Sort is to start by sorting elements that are far apart from each other and then gradually reducing the gap between the elements being compared. By doing this, it helps to bring elements closer to their intended position much faster than other sorting methods. This gap reduction strategy is what gives Shell Sort its improved performance characteristics compared to simpler sorting algorithms.

Shell Sort starts by choosing a gap, usually half the length of the array. Elements that are this gap apart are compared. If they're out of order, the smaller one is shifted to the left. This process is repeated for all elements separated by the gap. Once all pairs are compared for the current gap, the gap is reduced, usually halving it. The process continues with smaller and smaller gaps, refining the order each time. When the gap is finally reduced to 1, the algorithm performs an insertion sort on the nearly sorted array, completing the sorting efficiently.

![Shell Sort algorithm - visual representation](/SortingAlgorithms/ShellSort/res/shell_sort_visualization.png)

## Implementation
Here's an example implementation of the Shell Sort algorithm in Python: 

```python
from typing import List

def shell_sort(arr: List[int]) -> None:
    """
    Perform Shell Sort on a given list.

    Args:
        arr (List[int]): The list of elements to be sorted.

    Returns:
        None: The list is sorted in-place.
    """
    n = len(arr)
    gap = n //2  # Initialize the gap size

    # Continue sorting until the gap reduces to 0
    while gap > 0:
        print(f"\nGap:{gap}")
        # Perform a gapped insertion sort
        for i in range(gap, n):
            # Save the current element to be positioned
            temp = arr[i]
            j = i

             # Shift earlier gap-sorted elements up until the correct position is found
            shifted = False
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                shifted = True
                
            if shifted:
                arr[j] = temp

        # Reduce the gap for the next pass
        gap //= 2


# Example usage
sample_array = [5, 2, 9, 1, 7, 3, 8, 4, 6]
print("Original Array:", sample_array)
shell_sort(sample_array)
print("Sorted Array:", sample_array)
```

## Performances
**Time Complexity:**

- Best Case: O(n log n) – Achieved when the list is already partially sorted, minimizing swaps.
- Average Case: O(n^{3/2}) – Dependent on the choice of gap sequence.
- Worst Case: O(n^2) – Similar to insertion sort for poorly chosen gap sequences.

**Space Complexity:** O(1) – In-place sorting without additional data structures.
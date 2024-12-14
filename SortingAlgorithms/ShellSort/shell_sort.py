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
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
        print(f"Gap:{gap}")
        # Perform a gapped insertion sort
        for i in range(gap, n):
            # Save the current element to be positioned
            j = i - gap

            if arr[j] <= arr[i]:
                print("NoSwap")
            else:
                print(f"Swap {arr[i]} <> {arr[j]} ({j})")
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            print(f"{arr}")

        # Reduce the gap for the next pass
        gap //= 2

# Example usage
sample_array = [5, 2, 9, 1, 7, 3, 8, 4, 6]
print("Original Array:", sample_array)
shell_sort(sample_array)
print("Sorted Array:", sample_array)
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
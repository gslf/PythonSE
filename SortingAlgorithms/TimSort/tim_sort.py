from typing import List

MIN_RUN = 33

def insertion_sort(array: List[int], left: int, right: int) -> None:
    """Sort a section of the array using Insertion Sort."""
    for i in range(left + 1, right + 1):
        key = array[i]
        j = i - 1
        while j >= left and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def merge(array: List[int], left: int, mid: int, right: int) -> None:
    """Merge two sorted subarrays into one sorted segment."""
    left_part = array[left:mid + 1]
    right_part = array[mid + 1:right + 1]

    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        array[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        array[k] = right_part[j]
        j += 1
        k += 1

def tim_sort(array: List[int]) -> None:
    """Sort the array using TimSort algorithm."""
    n = len(array)

    # Divide the array into runs of size MIN_RUN and sort each run
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(array, start, end)

    # Merge runs iteratively
    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(array, left, mid, right)
        size *= 2

# Example usage
if __name__ == "__main__":
    arr = [5, 2, 3, 8, 7, 6, 1, 4]
    tim_sort(arr)
    print(arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
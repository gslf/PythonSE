def heapify(arr, n, i):
    # Find the largest among current node, left child, and right child
    largest = i  # Initially assume the current node is the largest
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if the left child is larger than the current node
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right child is larger than the current (or left if already changed)
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the current node, swap and continue heapify
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
arr = [64, 5, 25, 12, 22, 11, 90]
heap_sort(arr)
print("Sorted array:", arr)

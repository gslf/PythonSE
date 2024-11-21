class MaxHeap:
    def __init__(self):
        """
        Initialize an empty Max Heap.
        """
        self.heap = []

    def _parent(self, index):
        """
        Get the index of the parent node.
        """
        return (index - 1) // 2

    def _left_child(self, index):
        """
        Get the index of the left child node.
        """
        return 2 * index + 1

    def _right_child(self, index):
        """
        Get the index of the right child node.
        """
        return 2 * index + 2

    def _heapify_up(self, index):
        """
        Restore the heap property by moving the node at index up.
        """
        parent = self._parent(index)
        if index > 0 and self.heap[index] > self.heap[parent]:
            # Swap with the parent if the current node is greater
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """
        Restore the heap property by moving the node at index down.
        """
        largest = index
        left = self._left_child(index)
        right = self._right_child(index)

        # Check if the left child is larger
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        # Check if the right child is larger
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # If the largest is not the current node, swap and continue heapifying
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def insert(self, value):
        """
        Insert a new value into the heap.
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """
        Remove and return the maximum value from the heap.
        """
        if not self.heap:
            raise IndexError("extract_max() called on empty heap")
        # Swap the max with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_value = self.heap.pop()
        # Restore the heap property
        self._heapify_down(0)
        return max_value





# Example usage:
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(15)
print("MaxHeap:", max_heap.heap)
print("Extracted max:", max_heap.extract_max())
print("MaxHeap after extraction:", max_heap.heap)



from typing import List, Callable

class SegmentTree:
    """
    A basic implementation of a Segment Tree for range queries and updates.

    Attributes:
    - arr: List[int] - The input array for which the segment tree is built.
    - tree: List[int] - The segment tree array storing intermediate results.
    - operation: Callable - The associative operation used in the segment tree (e.g., sum, min, max).
    - default: int - The default value for the operation (e.g., 0 for sum).
    """

    def __init__(self, arr: List[int], operation: Callable[[int, int], int], default: int):
        """
        Initializes the SegmentTree with an input array, operation, and default value.

        Args:
        - arr: List[int] - The input array.
        - operation: Callable - An associative operation for range queries.
        - default: int - Default value for segments outside the query range.
        """
        self.arr = arr  # Original array.
        self.n = len(arr)  # Number of elements in the array.
        self.tree = [default] * (4 * self.n)  # Segment tree structure (size 4*n ensures enough space).
        self.operation = operation  # The operation used for range queries (e.g., sum, min, max).
        self.default = default  # Default value for operation (e.g., 0 for sum).
        self._build(0, 0, self.n - 1)  # Build the segment tree.

    def _build(self, node: int, start: int, end: int):
        """
        Recursively builds the segment tree.

        Args:
        - node: int - Current node index in the segment tree.
        - start: int - Start index of the range this node represents.
        - end: int - End index of the range this node represents.
        """
        if start == end:
            # Leaf node, directly assign the value from the array.
            self.tree[node] = self.arr[start]
        else:
            # Internal node, divide the range into two halves.
            mid = (start + end) // 2
            # Recursively build the left child.
            self._build(2 * node + 1, start, mid)
            # Recursively build the right child.
            self._build(2 * node + 2, mid + 1, end)
            # Combine the results of the two children using the operation.
            self.tree[node] = self.operation(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def _query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        """
        Recursively performs a range query on the segment tree.

        Args:
        - node: int - Current node index in the segment tree.
        - start: int - Start index of the range this node represents.
        - end: int - End index of the range this node represents.
        - l: int - Start index of the query range.
        - r: int - End index of the query range.

        Returns:
        - int: Result of the operation over the query range.
        """
        if r < start or l > end:
            # Query range does not intersect this segment; return the default value.
            return self.default
        if l <= start and end <= r:
            # Current segment is completely within the query range.
            return self.tree[node]
        # Partial overlap: query both children.
        mid = (start + end) // 2
        left_result = self._query(2 * node + 1, start, mid, l, r)
        right_result = self._query(2 * node + 2, mid + 1, end, l, r)
        # Combine the results from both children.
        return self.operation(left_result, right_result)

    def query(self, l: int, r: int) -> int:
        """
        Public method to perform a range query on the segment tree.

        Args:
        - l: int - Start index of the query range.
        - r: int - End index of the query range.

        Returns:
        - int: Result of the operation over the range [l, r].
        """
        return self._query(0, 0, self.n - 1, l, r)

    def _update(self, node: int, start: int, end: int, index: int, value: int):
        """
        Recursively updates the segment tree with a new value at a given index.

        Args:
        - node: int - Current node index in the segment tree.
        - start: int - Start index of the range this node represents.
        - end: int - End index of the range this node represents.
        - index: int - Index of the array to update.
        - value: int - New value to set at the index.
        """
        if start == end:
            # Leaf node, update the value.
            self.tree[node] = value
        else:
            # Internal node, determine which child to update.
            mid = (start + end) // 2
            if start <= index <= mid:
                # Update left child.
                self._update(2 * node + 1, start, mid, index, value)
            else:
                # Update right child.
                self._update(2 * node + 2, mid + 1, end, index, value)
            # Recalculate the value of the current node using the operation.
            self.tree[node] = self.operation(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, index: int, value: int):
        """
        Public method to update a value in the segment tree.

        Args:
        - index: int - Index of the array to update.
        - value: int - New value to set at the index.
        """
        self.arr[index] = value  # Update the value in the original array.
        self._update(0, 0, self.n - 1, index, value)  # Update the segment tree.

# Example Usage
if __name__ == "__main__":
    arr = [5, 2, 9, 1, 7, 3]
    seg_tree = SegmentTree(arr, operation=lambda x, y: x + y, default=0)
    print(seg_tree.tree)  # The segment tree structure.

    print(seg_tree.query(1, 4))  # Output: 24 (sum of elements in range [1, 4]).
    seg_tree.update(3, 6)  # Update index 3 with value 6.
    print(seg_tree.query(1, 4))  # Output: 23 (updated sum of elements in range [1, 4]).

from typing import List

class FenwickTree:
    def __init__(self, size: int):
        """Initialize a Fenwick Tree with given size.
        
        Args:
            size: The size of the underlying array
        """
        self.size: int = size
        self.tree: List[int] = [0] * (size + 1)  # 1-based indexing
    
    def update(self, index: int, delta: int) -> None:
        """Update value at index by adding delta.
        
        Args:
            index: The 0-based index to update
            delta: The value to add (can be negative)
        """
        index += 1  # Convert to 1-based indexing
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)  # Add LSB to move to parent
    
    def prefix_sum(self, index: int) -> int:
        """Get sum of elements from index 0 to given index.
        
        Args:
            index: The 0-based index to calculate prefix sum up to
        Returns:
            The sum of elements from 0 to index
        """
        index += 1  # Convert to 1-based indexing
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)  # Remove LSB to move to parent
        return total
    
    def range_sum(self, left: int, right: int) -> int:
        """Get sum of elements between left and right indices (inclusive).
        
        Args:
            left: The left boundary (0-based)
            right: The right boundary (0-based)
        Returns:
            The sum of elements in the range [left, right]
        """
        return self.prefix_sum(right) - (
            self.prefix_sum(left - 1) if left > 0 else 0
        )
    
    @classmethod
    def from_array(cls, arr: List[int]) -> 'FenwickTree':
        """Create a Fenwick Tree from an array.
        
        Args:
            arr: The input array
        Returns:
            A new FenwickTree instance initialized with the array
        """
        tree = cls(len(arr))
        for i, val in enumerate(arr):
            tree.update(i, val)
        return tree
    
# Test case 1: Basic operations
print("Test Case 1: Basic Operations")
arr = [3, 2, 5, 1, 4, 7, 6, 8]
ft = FenwickTree.from_array(arr)
print(f"Tree array: {ft.tree}\n")

# Test prefix sums
print(f"Original array: {arr}")
print(f"Prefix sum at index 3: {ft.prefix_sum(3)}")  # Should be 11 (3+2+5+1)
print(f"Prefix sum at index 7: {ft.prefix_sum(7)}")  # Should be 36 (sum of all)

# Test range sums
print(f"Sum of range [2,5]: {ft.range_sum(2, 5)}\n")  # Should be 17 (5+1+4+7)

# Test update
print("\nTest Case 2: Update Operations")
original_sum = ft.prefix_sum(7)
print(f"Original sum of all elements: {original_sum}\n")

ft.update(4, 3)  # Add 3 to index 4 (value becomes 7)
new_sum = ft.prefix_sum(7)
print(f"Sum after updating index 4 with +3: {new_sum}\n")

# Test case 2: Edge cases
print("\nTest Case 3: Edge Cases")
# Single element range
print(f"Sum of range [3,3]: {ft.range_sum(3, 3)}")  # Should give single element
# First element
print(f"First element sum: {ft.range_sum(0, 0)}")
# Last element
print(f"Last element sum: {ft.range_sum(7, 7)}\n")

# Test case 3: Negative numbers
print("\nTest Case 4: Negative Numbers")
ft.update(2, -5)  # Subtract 5 from index 2
print(f"Sum after subtracting 5 from index 2: {ft.prefix_sum(7)}")
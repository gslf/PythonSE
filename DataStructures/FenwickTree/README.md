# Fenwick Tree in Python

The Fenwick Tree, also known as the Binary Indexed Tree (BIT), is a data structure that provides efficient methods for calculating prefix sums and updating elements in an array. This structure was introduced by Peter Fenwick in 1994 and is widely used in competitive programming and algorithm design due to its efficiency.

The Fenwick Tree operates on the principle of storing partial sums in a special binary representation. Unlike a traditional array that stores single values, each index in a Fenwick Tree maintains responsibility for a specific range of elements. The key insight lies in how these ranges are determined using the binary representation of indices.

A Fenwick Tree is typically represented as an array, where each index represents a node in the Fenwick Tree. The core idea behind Fenwick Trees is to store the partial sums of the array in a clever way that allows for efficient updates and queries. Specifically, each node in the tree stores the sum of a range of elements in the original array. The size of this range is determined by the least significant bit (LSB) of the node's index. For example, the node at index 8 (binary 1000) stores the sum of the elements from index 1 to 8. This is because the LSB of 8 is 000, which corresponds to a range of 8 elements.

### Key Components:

- **Storage Array:** A 1-based indexed array storing cumulative values
- **Binary Index Property:** Each index is responsible for a range determined by its least significant bit (LSB)
- **Parent-Child Relationship:** Defined by binary operations on indices

### Core Operations:

- **LSB Calculation:** Uses x & (-x) to isolate the least significant bit
- **Update Propagation:** Moves upward through parent nodes
- **Query Traversal:** Moves downward accumulating partial sums


## Structure example

Consider this array: **[3, 2, 5, 1, 4, 7, 6, 8]**

The binary representation of indices and their ranges is this:

| Index (binary) | Range Length | Responsible Range |
|----------------|--------------|-------------------|
| 1 (001)        | 1            | [1]               |
| 2 (010)        | 2            | [1-2]             |
| 3 (011)        | 1            | [3]               |
| 4 (100)        | 4            | [1-4]             |
| 5 (101)        | 1            | [5]               |
| 6 (110)        | 2            | [5-6]             |
| 7 (111)        | 1            | [7]               |
| 8 (1000)       | 8            | [1-8]             |

So the Fenwick Tree array is this: **[0, 3, 5, 5, 11, 4, 11, 6, 36]**

![Fenwick Tree - visual representation](/DataStructures/FenwickTree/res/fenwick_tree_visualization.png)

## Python Implementation
```python
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
```

## Performances Analysis
The key operations on Fenwick Trees have the following time complexities:

- Building the Fenwick Tree: O(n), where n is the size of the input array.
- Updating a single element: O(log n).
- Querying the sum of a range: O(log n).
- Calculating the prefix sum up to a given index: O(log n).
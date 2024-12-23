# Sparse Table in Python

A Sparse Table is a data structure designed to efficiently perform range queries (like minimum, maximum, sum, or GCD) on a static array. The name "sparse" comes from the fact that it doesn't store all possible ranges, but rather precomputes results for ranges whose lengths are powers of 2, making it memory-efficient while maintaining fast query times.

The core components of a Sparse Table include:

1. The input array of values
2. A 2D table storing precomputed results
3. A lookup array for quickly calculating log2 values

## How it works
Let's consider a real-world scenario where we need to find the minimum temperature recorded over any range of days.

![Sparse Table - visual representation](/DataStructures/SparseTable/res/sparse_table_visualization.png)

To find the minimum temperature between days 2 and 5 (0-based indexing):

1. Calculate range length: 4 (days 2,3,4,5)
2. Find largest power of 2 that fits: 2^2 = 4
3. Look up min(table[2][2], table[2][2]) = min(1, 1) = 1

## Implementation
```python
from typing import List, Callable
import math

class SparseTable:
    def __init__(self, arr: List[int], func: Callable[[int, int], int] = min):
        """
        Initialize Sparse Table with an array and an optional function (default: min).
        
        Args:
            arr: Input array
            func: Function to be applied on ranges (min, max, gcd, etc.)
        """
        self.n = len(arr)
        self.func = func
        self.log_table = [0] * (self.n + 1)
        self.k = int(math.log2(self.n)) + 1
        
        # Precompute log values
        for i in range(2, self.n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1
            
        # Initialize sparse table
        self.table = [[0] * self.k for _ in range(self.n)]
        
        # Fill in base cases (ranges of length 1)
        for i in range(self.n):
            self.table[i][0] = arr[i]
            
        # Build sparse table
        for j in range(1, self.k):
            for i in range(self.n - (2 ** j) + 1):
                self.table[i][j] = self.func(
                    self.table[i][j-1],
                    self.table[i + (2 ** (j - 1))][j-1]
                )
                
    
    def query(self, left: int, right: int) -> int:
        """
        Query the range [left, right] inclusive.
        
        Args:
            left: Left boundary of range
            right: Right boundary of range
            
        Returns:
            Result of applying func on the range
        """
        # Calculate the largest power of 2 that fits in the range
        j = self.log_table[right - left + 1]

        # Combine the two overlapping ranges
        return self.func(
            self.table[left][j],
            self.table[right - (2 ** j) + 1][j]
        )
        
    
# Example Usage

# Sample Array
arr = [4, 2, 7, 1, 8, 5, 3, 6]

# Test a Sparse Table with the min function
sparse_table_min = SparseTable(arr, min)
print(sparse_table_min.table)

print("Sparse Table Min")
print(sparse_table_min.query(2, 5)) # 1 
print(sparse_table_min.query(1, 3)) # 1
print(sparse_table_min.query(4, 6)) # 3 

# Test a Sparse Table with the max function
sparse_table_max = SparseTable(arr, max)

print("\nSparse Table Max")
print(sparse_table_max.query(0, 5)) # 8 
print(sparse_table_max.query(1, 3)) # 7   
print(sparse_table_max.query(4, 6)) # 8  
```

## Performances Analysis

**Preprocessing:**

- Time Complexity: O(n log n)
- Space Complexity: O(n log n)

**Query Operations:**

- Time Complexity: O(1) for idempotent functions (min, max, gcd)
- Time Complexity: O(log n) for non-idempotent functions (sum)
- Space Complexity: O(1)

The O(1) query time efficiency for idempotent functions (where overlapping ranges do not influence the result) positions Sparse Tables as the optimal solution for range minimum/maximum queries on static arrays. However, the O(n log n) preprocessing time and space requirements render it less suitable for data that undergoes frequent changes.
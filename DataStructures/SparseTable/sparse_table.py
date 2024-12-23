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
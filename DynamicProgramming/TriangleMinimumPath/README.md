# Triangle Minimum Path Sum with Dynamic Programming in Python

The Triangle Minimum Path Sum problem is a classic problem in algorithmic programming where we are given a triangle of integers, and our goal is to find the minimum path sum from the top of the triangle down to the base. 

The triangle data structure is a collection of numbers arranged in a triangular format. We need a method to traverse from top to bottom finding the minimum sum.

The key insight is that at each position, we only need to know the minimum path sum to reach that position. This overlapping subproblem structure makes it perfect for dynamic programming.

## How it works

To retrieve the path with the minimum sum of the triangle, we proceed according to these steps:

- **STEP 1:** Create a DP table, which in this case is an array, by copying the last row of the triangle.
- **STEP 2:** Start calculating the minimum paths from the second-to-last row. Add each value of the triangle to the minimum value of the two adjacent values in our DP table (dp[j], dp[j + 1]). Continue this process until all rows of the triangle have been processed.
- **STEP 3:** In the first element of the DP table, we find the minimum obtainable sum. To also obtain the path, we need to backtrack through the DP table, reconstructing for each element which value was chosen in the corresponding row of the triangle.

![Triangle Minimum Path Sum - Dynamic Programming visual representation](/DynamicProgramming/TriangleMinimumPath/res/triangle_minimum_path_visualization.png)

## Implementation
```pyhton
from typing import List, Tuple

def minimum_total(triangle: List[List[int]]) -> Tuple[int, List[int]]:
    """
    Calculate the minimum path sum from top to bottom in a triangle.
    
    Args:
        triangle: A list of lists representing the triangle structure
        
    Returns:
        int: The minimum path sum from top to bottom
        
    Time Complexity: O(n^2) where n is the height of the triangle
    Space Complexity: O(n) using bottom-up DP with optimized space
    """
    
    # Create a DP table with the size of the bottom row
    dp = triangle[-1].copy()
    
    # Fill the DP table
    # Start from the second last row and move upwards
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # For each position, choose the minimum of the two possible paths below
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    
    # OPTIONAL: Backtrack the DP table to find the path
    path = [triangle[0][0]]
    current_index = 0

    for i in range(len(triangle)-1):
        left = triangle[i+1][current_index] + min(dp[current_index:current_index+2])
        right = triangle[i+1][current_index+1] + min(dp[current_index+1:current_index+3])
        
        if left <= right:
            path.append(triangle[i+1][current_index])
        else:
            current_index += 1
            path.append(triangle[i+1][current_index])

    return (dp[0], path)

# Example usage
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

result, path = minimum_total(triangle)
print(f"Minimum path sum: {result}")  # Output: 11
print(f"Path: {path}")  # Output: [2, 3, 5, 1]
```

## Performances Analysis
Space Complexity is O(1) if we consider in-place modification of the triangle. If we need to keep the original triangle, then O(n), where n is the number of rows.

The algorithm scans each element of the triangle once. There are n*(n+1)/2 elements in the triangle where n is the number of rows. Thus, the time complexity is O(n^2).
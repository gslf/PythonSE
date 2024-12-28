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
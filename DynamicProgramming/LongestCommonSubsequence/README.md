# LCS (Longest Common Subsequence) problem - Dynamic Programming in Python

The Longest Common Subsequence (LCS) is a classic software engineering problem that finds the longest sequence of elements that appear in the same order in two different sequences. The Longest Common Subsequence is a sequence that appears in the same relative order but not necessarily contiguous, in two or more strings or lists. .

Consider two sequences:

X = "AGCAT"
Y = "GAC"

A subsequence is formed by taking elements from a sequence while maintaining their relative order. For Y, valid subsequences include "G", "GA", "GC", "AC", etc.

The longest common subsequence between X and Y is "AC" (length 2). Note how these characters appear in both strings in the same order, though not necessarily consecutively.

## How it Works

**STEP 1: Initialization** - Create a matrix where rows represent elements of one sequence and columns represent elements of the other. Initialize the first row and column with zeros.

**STEP 2: Filling the Matrix** - We then proceed to fill this grid row by row. For each pair of characters from the two sequences, if the characters match, we increase the count of the LCS taking the value from the upper left diagonal (i-1, j-1) and adding 1. If they don't match, we take the maximum length of the LCS that taking the maximum value between the upper value (i-1, j) and the left value (i, j-1).

**STEP3: Backtracking** - After filling the grid, we start from the bottom right cell, which holds the length of the LCS. We then move diagonally when characters match, or horizontally or vertically when they don't, collecting characters along the way. This process essentially reconstructs the longest common subsequence by following the path that contributed to the maximum value in our grid.

![Longest Common Subsequence Dynamic Programming - visual representation](/DynamicProgramming\LongestCommonSubsequence\res\longest_common_subsequence_visualization_visualization.png)

## Implementation
```pyhton
from typing import List, Tuple

def longest_common_subsequence(text1: str, text2: str) -> Tuple[str, List[List[int]]]:
    """
    Find the longest common subsequence between two strings using dynamic programming.
    
    Args:
        text1: First input string
        text2: Second input string
        
    Returns:
        Tuple containing the LCS string and the DP matrix
    """
    # Initialize the DP matrix with dimensions (m+1) x (n+1)
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                # If characters match, add 1 to the diagonal value
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # Take maximum of left and top cell
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Backtrack to find the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    return ''.join(reversed(lcs)), dp

# Example usage
text1 = "AGCAT"
text2 = "GAC"
result, matrix = longest_common_subsequence(text1, text2)

print(f"LCS: {result}")
```

## Performance Analysis
The LCS algorithm using dynamic programming has the following complexities:

- **Time Complexity:** O(m × n)
Where m and n are the lengths of the two input sequences.

- **Space Complexity:** O(m × n)

The efficient use of dynamic programming avoids the exponential time complexity that would result from a naive recursive approach. The memoization of previously computed results in the DP matrix ensures that each subproblem is solved only once.

The space complexity can be optimized to O(min(m,n)) if we only need the length of the LCS and not the actual sequence, as we only need to keep track of the previous row of the DP matrix.
# Edit Distance - Dynamic Programming in Python

The Levenshtein Distance, commonly known as Edit Distance, is a measure of the minimum number of single-character edits required to change one word into another. These edits can include insertions, deletions, or substitutions.

Dynamic programming resolves this by constructing a two-dimensional table where each cell (i, j) represents the edit distance between the first i characters of string A and the first j characters of string B. The solution builds upon previously computed distances, allowing for efficient calculation by considering the cost of each possible operation at each step. The final cell in the table contains the minimum edit distance for the two full strings.

## How It Works

**STEP 1: DP Table Initialization.**  matrix dp of dimensions (m+1) x (n+1) is initialized where m and n are the lengths of the two strings being compared. The first row and column are filled with incremental numbers to represent the cost of inserting or deleting all characters from one string to match the other.

**STEP 2: DP Table Processing.** If characters are the same, the value is copied from the diagonal (no operation needed). When characters differ between two strings, three operations can be considered to calculate the edit distance: insertion, deletion, and substitution. The insertion updates the value as dp[i][j] = dp[i][j-1] + 1, deletion as dp[i][j] = dp[i-1][j] + 1, and substitution as dp[i][j] = dp[i-1][j-1] + 1. The final value of dp[i][j] is the minimum of these three options.

![Edit Distance - Dynamic Programming visual representation](/DynamicProgramming/EditDistance/res/edit_distance_visualization.png)

## Implementation
```python
from typing import List

def edit_distance(str1: str, str2: str) -> int:
    """
    Calculate the Edit (Levenshtein) distance between two strings using dynamic programming.

    Args:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    int: The minimum number of edits needed to transform str1 into str2.
    """
    m, n = len(str1), len(str2)
    # Initialize the matrix with an extra row and column for empty string cases
    dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the first column and row
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                               dp[i][j - 1] + 1,    # Insertion
                               dp[i - 1][j - 1] + 1)  # Substitution

    return dp[m][n]

# Example usage
print(edit_distance("kitten", "sitting"))  # Output 3
```

## Performances AnalysisTime Complexity Analysis

The overall time complexity of the Levenshtein Distance algorithm using dynamic programming is** O(m*n)**, where m and n are the lengths of the strings being compared. This approach significantly improves upon the brute force method which would have an exponential complexity.
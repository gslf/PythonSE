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
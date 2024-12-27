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
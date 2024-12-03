def knapsack(values, weights, capacity):
    """
    Solves the 0/1 Knapsack Problem using Dynamic Programming.

    :param values: List of item values.
    :param weights: List of item weights.
    :param capacity: Maximum weight capacity of the knapsack.
    :return: Maximum value achievable within the given weight capacity.
    """
    # Number of items
    n = len(values)
    
    # Initialize a DP table with dimensions (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table row by row
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # Item can fit in the knapsack
                # Include the item or exclude it, whichever gives more value
                dp[i][w] = max(dp[i - 1][w], + dp[i - 1][w - weights[i - 1]])
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]
    
    # The bottom-right corner contains the maximum value
    return dp[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [1, 2, 3]
capacity = 4

max_value = knapsack(values, weights, capacity)
print(f"Maximum value achievable: {max_value}")

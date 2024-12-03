# Optimizing the Knapsack Problem with Dynamic Programming in Python 

The Knapsack Problem is a classic optimization challenge. The task is simple: given a set of items, each with a weight and a value, determine the maximum value you can achieve by selecting items without exceeding a weight limit.

Dynamic programming breaks down problems into overlapping subproblems and solves each subproblem only once, storing the results for future reference. For the Knapsack Problem, we use a bottom-up approach to build a solution incrementally:

1. Divide the problem into smaller subproblems, each representing a decision to include or exclude an item.
2. Use a table to store solutions for subproblems, avoiding redundant computations.
3. Combine solutions from subproblems to solve the larger problem efficiently.

## The algorithm to solve the problem

Think of the DP table as a grid where:
- Rows represent items (including a "no-item" row for base cases).
- Columns represent weight capacities from 0 to the given maximum.

Each cell dp[i][w] stores the maximum value achievable using the first w.

T Solution Step-by-Step:
1. Start from an empty knapsack: The first row and column are initialized to 0 since no items or weight capacity yields no value.
2. Evaluate each item: For each subsequent row, ask:
    - If I include this item, what's the best value I can achieve?
    - If I exclude it, what's the value from previous computations?
3. Pick the better option: Update each cell based on whether including the current item improves the total value.


![KnapsackProblem - visual representation](/DynamicProgramming/KnapsackProblem/res/0_1_knapsack.png)

## Implementation

```python
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
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]
    
    # The bottom-right corner contains the maximum value
    return dp[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = knapsack(values, weights, capacity)
print(f"Maximum value achievable: {max_value}")
```
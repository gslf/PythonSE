# Interval Scheduling - Dynamic Programming in Python

Interval Scheduling is a classic optimization problem that involves selecting a subset of mutually compatible intervals (or tasks) from a given set, where each interval has a start time, end time, and possibly a weight (or profit). The goal is to maximize the total weight of the selected intervals while ensuring no two intervals overlap.

## How it works
In the Weighted Interval Scheduling Problem (WISP) each interval is represented as (start, end, weight). 

**STEP 1 -** Sort intervals by their end times to ensure a well-defined order.

**STEP 2 -** for each interval i, find the largest index j such that interval j is compatible with interval i (i.e., end[j] <= start[i]). This can be done efficiently using binary search.

**STEP 3 -** Process the DP table. For each interval i, we calculate the maximum profit by considering two options. The first option is to exclude interval i, in which case the profit remains the same as dp[i−1]. The second option is to include interval i, where the profit is determined by the weight of interval i (given by intervals[i−1][2]) plus the profit from the best compatible subset found in dp[p[i−1]+1].

**STEP 4 -** Backtrack the DP table to reconstruct the best combination of appointments.

![Interval Scheduling - Dynamic Programming visual representation](/DynamicProgramming/IntervalScheduling/res/interval_scheduling_visualization.png)

## Implementation
```python
from typing import List, Tuple
import bisect

# Define a type alias for intervals
Interval = Tuple[int, int, int]  # (start, end, weight)

def weighted_interval_scheduling(intervals: List[Interval]) -> Tuple[int, List[Interval]]:
    # Step 1: Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])
    
    # Step 2: Precompute the 'p' array (last compatible interval for each interval)
    n = len(intervals)
    p = [0] * n
    for i in range(n):
        # Binary search to find the last compatible interval
        p[i] = bisect.bisect_right([intervals[j][1] for j in range(i)], intervals[i][0]) - 1
    
    # Step 3: process DP table
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # Option 1: Exclude the current interval
        exclude = dp[i - 1]
        # Option 2: Include the current interval
        previous_value = intervals[i - 1][2]
        has_previous = p[i - 1] >= 0
        additional_value = dp[p[i - 1] + 1] if has_previous else 0
        include = previous_value + additional_value
        
        # Choose the better option
        dp[i] = max(exclude, include)

    # Step 4: Backtrack the DP table to reconstruct the solution
    result = []
    i = n
    while i > 0:
        if dp[i] == dp[i - 1]:
            # Current interval not included
            i -= 1
        else:
            # Current interval included
            result.append(intervals[i - 1])
            i = p[i - 1] + 1

    result.reverse()  # Reverse to maintain original order
    return dp[n], result

# Example usage
intervals = [
    (5, 8, 150),
    (1, 3, 50),
    (2, 5, 20),
    (4, 6, 100),
    (6, 7, 200),
]

max_profit, selected_intervals = weighted_interval_scheduling(intervals)
print(f"Maximum Profit: {max_profit}")
print("Selected Intervals:", selected_intervals)
```

## Performances Analysis

Sorting the intervals by end time takes **O(n log n)**. Precomputing Compatibility (p array) for each interval takes **O(n log n)**. Filling the DP table requires O(n) iterations, where each iteration performs constant-time operations. The dominant terms are sorting and compatibility computation, so the overall complexity is O(n log n).
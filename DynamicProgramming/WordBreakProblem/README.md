# Word Break Problem - Dynamic Programming in Python

The Word Break Problem is a classic algorithmic challenge that demonstrates the power of dynamic programming. Given a string and a dictionary of valid words, the problem asks whether the string can be segmented into a sequence of valid words from the dictionary. This problem is particularly relevant in natural language processing, text analysis, and computational linguistics.

Consider the input string "ilikeprogramming" and a dictionary containing words like ["i", "like", "programming"]. The challenge is to determine if we can break the input string into valid words from our dictionary. In this case, the answer would be "true" because we can break it into "i like programming".

The solution employs dynamic programming with these key components:

A boolean DP array where dp[i] represents whether the substring from index 0 to i can be segmented into valid words
A dictionary (typically implemented as a set) containing valid words
A bottom-up approach to build the solution

## How it Works

Let's break down how the algorithm works with this data:

**String:** "hellopython"
**Dictionary:** ["hello", "python"]


![Word Break Problem - Dynamic Programming Visual Representation](/DynamicProgramming/WordBreakProblem/res/word_break_problem_visualization.png)

## Implementation
```python
```

## Performances Analysis

#### Space Complexity: O(n)
We use a DP array of size n+1, where n is the length of the input string. The word set takes additional space but is bound by the dictionary size.

#### Time Complexity: O(n²)
For each position i (0 to n), we try all possible previous positions j (0 to i). String slicing and set lookup operations are O(1) on average. Overall complexity is O(n²) due to the nested loops.

### Preprocessing: O(m)
Converting the word list to a set takes O(m) time, where m is the total length of all words in the dictionary.
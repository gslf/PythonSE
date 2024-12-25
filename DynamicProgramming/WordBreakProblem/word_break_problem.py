from typing import List, Set

def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Determines if a string can be segmented into words from the dictionary.
    
    Args:
        s: The input string to be segmented
        word_dict: List of valid words
    
    Returns:
        bool: True if the string can be segmented, False otherwise
    """
    # Convert word_dict to set for O(1) lookup
    word_set: Set[str] = set(word_dict)
    
    # dp[i] represents if s[:i] can be segmented into valid words
    dp: List[bool] = [False] * (len(s) + 1)
    dp[0] = True  # Empty string is always valid
    
    # For each position in the string
    for i in range(1, len(s) + 1):
        # Try all possible words ending at position i
        for j in range(i):
            print(f"{i}:{j} - {s[j:i]}")
            # If we can segment string up to j and substring from j to i is in dictionary
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    print("----------------------")
    print("Dictionary: ", word_dict)
    print("String: ", s)
    print("DP Table: ", dp)

    return dp[len(s)]



# Example usage

# Test case 1: Simple positive scenario
test1 = word_break("hellopython", ["hello", "python"])  
print(test1) # Output: True

# Test case 2: Simple negative scenario
test2 = word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
print(f"Test 2 result: {test2}") # Output: False
    
# Test case 3: Empty string
test3 =  word_break("", ["cat", "dog"]) 
print(test3) # Output: True
    
test4 = word_break("applepenapple", ["apple", "pen"]) 
print(test4) # Output: True
    
test5 = word_break("catsandog", ["cats", "dog", "sand"])
print(test5) # Output: False
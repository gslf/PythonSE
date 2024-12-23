# Bloom Filter in Python
A Bloom filter is a space-efficient probabilistic data structure designed to rapidly test whether an element is a member of a set. Created by Burton Howard Bloom in 1970, it's useful to represent a set of elements where space efficiency is crucial and where false positives are acceptable but false negatives are not.

**Key advantages:**

- Constant time operations regardless of the number of elements
- Space efficiency compared to traditional hash tables
- No false negatives (if an element is reported as absent, it is definitely absent)

**Main trade-off:**

- Possibility of false positives (an element might be reported as present when it's not)
- Cannot remove elements (removal could create false negatives)

## How it works
You're right. Let me provide a practical, step-by-step visual explanation of how a Bloom filter works.

Visual Guide to Bloom Filters
Let's track exactly what happens when we create a Bloom filter with:

8 bits (for simplicity)
2 hash functions (h1 and h2)

**Goal: store and check for email addresses in a spam filter**

```
INITIAL STATE
Bit Array: [0 0 0 0 0 0 0 0]
Positions:  0 1 2 3 4 5 6 7
```

Adding email "spam@mail.com"

- Apply hash function h1("spam@mail.com") = 2
- Apply hash function h2("spam@mail.com") = 5

```
Bit Array: [0 0 1 0 0 1 0 0]
Positions:  0 1 2 3 4 5 6 7
              ^     ^
              |     |
              h1    h2
```

Adding another email "scam@mail.com"

- Apply h1("scam@mail.com") = 1
- Apply h2("scam@mail.com") = 5

```
Bit Array: [0 1 1 0 0 1 0 0]
Positions:  0 1 2 3 4 5 6 7
              ^ ^     ^
              | |     |
              | h1    h2 (overlaps with previous)
              new bit set
```
#### Checking membership

Case 1: Checking "spam@mail.com"
- h1("spam@mail.com") = 2 → bit is 1 ✓
- h2("spam@mail.com") = 5 → bit is 1 ✓

**Result: Might be in set (true positive)**

Case 2: Checking "good@mail.com"
- h1("good@mail.com") = 3 → bit is 0 ✗
- h2("good@mail.com") = 6 → bit is 0 ✗

**Result: Definitely not in set**

Case 3: False Positive Example "test@mail.com"

- h1("test@mail.com") = 1 → bit is 1 ✓
- h2("test@mail.com") = 5 → bit is 1 ✓

**Result: Might be in set (false positive, because these bits were set by other emails)**

#### Why False Positives Occur


```
Multiple emails can set same bit

Initial:           [0 0 0 0 0 0 0 0]
After spam@mail:   [0 0 1 0 0 1 0 0]
After scam@mail:   [0 1 1 0 0 1 0 0]
                      ↑ ↑     ↑
                      | |     |
                      | |     +-- Bits remain set
                      | +-------- Bits remain set
                      +---------- New bits get set
```

When we check "test@mail.com", it happens to hash to positions that were set by the combination of previous emails, even though we never added it. This is why Bloom filters can have false positives but never false negatives - if any bit is 0, we know for certain the element was never added.


## Implementation
```python
from typing import Any
import math

class BloomFilter:
    def __init__(self, expected_elements: int, false_positive_rate: float):
        """
        Initialize a Bloom Filter.
        
        Args:
            expected_elements: Number of expected elements to be inserted
            false_positive_rate: Desired false positive rate (between 0 and 1)
        """
        # Calculate optimal size of bit array
        self.size = self._get_size(expected_elements, false_positive_rate)
        # Calculate optimal number of hash functions
        self.hash_count = self._get_hash_count(self.size, expected_elements)
        # Initialize bit array
        self.bit_array = [0] * self.size
        
    def _get_size(self, n: int, p: float) -> int:
        """Calculate optimal size of bit array."""
        return int(-n * math.log(p) / (math.log(2) ** 2))
    
    def _get_hash_count(self, m: int, n: int) -> int:
        """Calculate optimal number of hash functions."""
        return int((m / n) * math.log(2))
    
    def _custom_hash(self, element: Any, seed: int) -> int:
        """
        Custom hash function to replace mmh3.
        Uses a simple but effective hashing algorithm.
        
        Args:
            element: Element to hash
            seed: Seed for generating different hash values
        
        Returns:
            int: Hash value
        """
        # Convert element to string and hash it with a custom method
        element_str = str(element)
        
        # Base hash using a simple polynomial rolling hash
        hash_value = 0
        for char in element_str:
            # Use seed to modify the hash generation
            hash_value = (hash_value * (seed + 31) + ord(char)) & 0xFFFFFFFF
        
        # Add some bit mixing to improve distribution
        hash_value ^= hash_value >> 16
        hash_value *= 0x85ebca6b
        hash_value ^= hash_value >> 13
        hash_value *= 0xc2b2ae35
        hash_value ^= hash_value >> 16
        
        return hash_value
    
    def add(self, element: Any) -> None:
        """
        Add an element to the Bloom filter.
        
        Args:
            element: Element to be added
        """
        for seed in range(self.hash_count):
            index = self._custom_hash(element, seed) % self.size
            self.bit_array[index] = 1
            
    def contains(self, element: Any) -> bool:
        """
        Check if an element might be in the set.
        
        Args:
            element: Element to check
        
        Returns:
            bool: True if element might be present, False if definitely absent
        """
        for seed in range(self.hash_count):
            index = self._custom_hash(element, seed) % self.size
            if self.bit_array[index] == 0:
                return False
        return True

# Esempio di utilizzo

bloom = BloomFilter(1000, 0.01)


bloom.add("apple")
bloom.add("banana")
bloom.add("cherry")


print(bloom.contains("apple"))    # True
print(bloom.contains("banana"))   # True
print(bloom.contains("date"))     # False (probably)
```


## Performances Analysis
Operations on a Bloom filter have the following time complexities:

- **Initialization:** O(m) where m is the size of the bit array
- **Add element:** O(k) where k is the number of hash functions
- **Check membership:** O(k) where k is the number of hash functions

Space complexity is O(m) where m is the size of the bit array.


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


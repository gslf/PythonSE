# Hash Table in Python

A **hash table** is a data structure that is used to store **keys/value pairs**. Each key is passed through a hash function, which returns an index in the array, and the value associated with the key is stored at that index. A **hash function** is any function that can be used to map a data set of an arbitrary size to a data set of a fixed size.

The strength of hash tables comes from their ability to provide constant-time access and their effective handling of large datasets. The hash function determines the index where a particular key-value pair will reside. When keys hash to the same index (a collision), a resolution strategy is employed to keep the data accessible.

![Hash Table - visual representation](/DataStructures/HashTable/res/hash_table_visualization.png)


Understanding hash tables can be aided by visualizing a line of boxes, each with an address. When we need to insert a value, we have a machine (the hash function) that tells us in which box to place it. Each key runs through this hash function and receives a unique box number, where the value gets stored.

## Collision Resolutions
Hash tables can encounter collisions when multiple keys map to the same index. Collision resolution strategies help manage these conflicts, and here are three of the most common methods: Chaining, Open Addressing, and Rehashing.

- **Linear Probing** is like looking for a parking spot when your preferred space is taken. If spot number 5 is occupied, you simply check spot 6. If that's also taken, you look at spot 7, and so on until you find an empty space. It's straightforward but can lead to clusters of occupied spots.
- **Quadratic Probing**  is similar to linear probing, but instead of checking the next spot, you check spots that are progressively further away, helping to avoid clusters
- **Chaining** is like having a stack of boxes at each location. When two items want the same spot, you just stack them together.


## Implementation
Here is a simple implementation of a HashTable that use linear probing as collision resolution strategy:

```python
class HashTable:
    def __init__(self, size=10):
        """
        Initialize the hash table with a fixed size.
        Args:
            size (int): The initial size of the hash table.
        """
        self.size = size
        self.table = [None] * self.size
        
    def hash_function(self, key):
        """
        Compute the hash for the given key.
        Args:
            key (str): The key to hash.
        Returns:
            int: The hash value, representing the index in the table.
        """
        return hash(key) % self.size
    
    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        Args:
            key (str): The key associated with the value.
            value (Any): The value to insert.
        """
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                # Update the value if the key already exists
                self.table[index] = (key, value)
                return
            # Linear probing
            index = (index + 1) % self.size
            if index == original_index:
                # Table is full
                raise Exception("HashTable is full")
        self.table[index] = (key, value)

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        Args:
            key (str): The key whose value needs to be fetched.
        Returns:
            Any: The value associated with the key.
        """
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            # Linear probing
            index = (index + 1) % self.size
            if index == original_index:
                # We've looped back around to the start
                break
        raise KeyError(f"Key '{key}' not found in HashTable")
    
    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        Args:
            key (str): The key to delete.
        """
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                # Mark as deleted with a sentinel value
                self.table[index] = None
                return
            # Linear probing
            index = (index + 1) % self.size
            if index == original_index:
                break
        raise KeyError(f"Key '{key}' not found in HashTable")
    
# Example code
hash_table = HashTable(size=5)
hash_table.insert("apple", 10)
print(hash_table.get("apple"))  # Output: 10
hash_table.insert("apple", 15)
print(hash_table.get("apple"))  # Output: 15
hash_table.delete("apple")
```
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

################  
# Example code #
################
hash_table = HashTable(size=5)
hash_table.insert("apple", 10)
print(hash_table.get("apple"))  # Output: 10
hash_table.insert("strawberry", 15)
print(hash_table.get("strawberry"))  # Output: 15
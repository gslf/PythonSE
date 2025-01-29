import random

class Node:
    """Represents a single node in a Skip List."""
    def __init__(self, key, level):
        self.key = key  # The value of the node
        self.forward = [None] * (level + 1)  # Forward pointers for each level

class SkipList:
    """A simple implementation of a Skip List data structure."""
    def __init__(self, max_level, p):
        self.max_level = max_level  # Maximum level of the skip list
        self.p = p  # Probability for level generation
        self.head = Node(None, max_level)  # Head node with maximum level
        self.level = 0  # Current level of the skip list

    def random_level(self):
        """Generates a random level for a new node."""
        level = 0
        while (random.random() < self.p 
               and level < self.max_level):
            level += 1
        return level

    def insert(self, key):
        """Inserts a key into the Skip List."""
        update = [None] * (self.max_level + 1)  # Track nodes that need updating
        current = self.head

        # Traverse the Skip List to find the position to insert
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        # Determine the level for the new node
        level = self.random_level()
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.head
            self.level = level

        # Create and insert the new node
        new_node = Node(key, level)
        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, key):
        """Searches for a key in the Skip List. Returns True if found, otherwise False."""
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[0]
        return current and current.key == key

    def delete(self, key):
        """Deletes a key from the Skip List, if it exists."""
        update = [None] * (self.max_level + 1)
        current = self.head

        # Traverse the Skip List to find the node to delete
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]
        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1

##################
# Example usage: # 
##################

skiplist = SkipList(max_level=4, p=0.5)
for num in [1, 3, 7, 8, 10]:
    skiplist.insert(num)

print(skiplist.search(8))  # Output: True
print(skiplist.search(5))  # Output: False
skiplist.delete(8)
print(skiplist.search(8))  # Output: False
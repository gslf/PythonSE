# Node class represents a single node in the binary search tree.
class Node:
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.left = None    # Pointer to the left child node
        self.right = None   # Pointer to the right child node

# BinarySearchTree class represents the binary search tree structure.
# It ensures that all nodes follow the binary search property.
class BinarySearchTree:
    def __init__(self):
        self.root = None  # The root node of the binary search tree (initially empty)

    # Method to insert a value into the binary search tree
    def insert(self, value):
        if self.root is None:
            # If the tree is empty, set the root to a new node with the given value
            self.root = Node(value)
        else:
            # Otherwise, delegate the insertion to the helper method
            self._insert(self.root, value)

    # Helper method to recursively insert a value into the correct position
    def _insert(self, current, value):
        if value < current.value:
            # If the value is less than the current node's value, go to the left subtree
            if current.left is None:
                current.left = Node(value)  # Create a new node if left child is empty
            else:
                self._insert(current.left, value)  # Recursively insert into the left subtree
        else:
            # If the value is greater or equal, go to the right subtree
            if current.right is None:
                current.right = Node(value)  # Create a new node if right child is empty
            else:
                self._insert(current.right, value)  # Recursively insert into the right subtree

    # Method to perform an in-order traversal of the tree
    # In-order traversal visits nodes in ascending order
    def inorder(self):
        return self._inorder(self.root)

    # Helper method to perform a recursive in-order traversal
    def _inorder(self, node):
        if node is None:
            return []
        # Traverse the left subtree, visit the current node, and then traverse the right subtree
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

    # Method to search for a value in the binary search tree
    def search(self, value):
        return self._search(self.root, value)

    # Helper method to recursively search for a value in the tree
    def _search(self, current, value):
        if current is None:
            # If the current node is None, the value is not found
            return False
        if value == current.value:
            # If the value matches the current node's value, it is found
            return True
        elif value < current.value:
            # If the value is less, search in the left subtree
            return self._search(current.left, value)
        else:
            # If the value is greater, search in the right subtree
            return self._search(current.right, value)

# Example usage:
bst = BinarySearchTree()
bst.insert(10)  # Insert root node with value 10
bst.insert(5)   # Insert value 5 to the left of 10
bst.insert(15)  # Insert value 15 to the right of 10
bst.insert(7)   # Insert value 7 to the right of 5

# Print the in-order traversal (sorted order of elements)
print(bst.inorder())  # Output: [5, 7, 10, 15]

# Search for specific values in the tree
print(bst.search(7))   # Output: True (7 exists in the tree)
print(bst.search(3))   # Output: False (3 does not exist in the tree)

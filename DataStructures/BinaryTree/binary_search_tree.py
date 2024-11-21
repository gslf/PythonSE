class Node:
    def __init__(self, key):
        self.key = key        # The key or value of the node
        self.left = None      # Left child
        self.right = None     # Right child

class BinarySearchTree:
    def __init__(self):
        self.root = None      # Root node of the BST

    def insert(self, key):
        """
        Inserts a new node with the given key into the BST.
        """
        if self.root is None:
            self.root = Node(key)  # If tree is empty, set new node as root
        else:
            self._insert(self.root, key)  # Call helper method to find the correct position

    def _insert(self, current_node, key):
        """
        Helper method for insert operation.
        """
        if key < current_node.key:
            # Key should be placed in the left subtree
            if current_node.left is None:
                current_node.left = Node(key)  # Insert new node if spot is available
            else:
                self._insert(current_node.left, key)  # Recurse on the left child
        elif key > current_node.key:
            # Key should be placed in the right subtree
            if current_node.right is None:
                current_node.right = Node(key)  # Insert new node if spot is available
            else:
                self._insert(current_node.right, key)  # Recurse on the right child
        else:
            # Duplicate keys are not allowed in BST
            pass  # Key already exists; do nothing

    def search(self, key):
        """
        Searches for a node with the given key in the BST.
        Returns True if found, False otherwise.
        """
        return self._search(self.root, key)

    def _search(self, current_node, key):
        """
        Helper method for search operation.
        """
        if current_node is None:
            return False  # Reached a leaf node; key not found
        if key == current_node.key:
            return True   # Key found
        elif key < current_node.key:
            return self._search(current_node.left, key)  # Search in the left subtree
        else:
            return self._search(current_node.right, key)  # Search in the right subtree

    def inorder_traversal(self):
        """
        Performs in-order traversal of the BST.
        Returns a list of keys in ascending order.
        """
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, current_node, result):
        """
        Helper method for in-order traversal.
        """
        if current_node:
            self._inorder_traversal(current_node.left, result)   # Visit left subtree
            result.append(current_node.key)                      # Visit node
            self._inorder_traversal(current_node.right, result)  # Visit right subtree
        return result

# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    # Insert keys into the BST
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)

    # Search for a key in the BST
    print("Search for 60:", bst.search(60))  # Output: True
    print("Search for 25:", bst.search(25))  # Output: False

    # Perform in-order traversal
    print("In-order Traversal:", bst.inorder_traversal())  # Output: [20, 30, 40, 50, 60, 70, 80]

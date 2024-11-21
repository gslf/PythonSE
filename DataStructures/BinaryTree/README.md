# Binary Tree in Python

A **binary tree** is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child. This structure is widely used in various applications, such as expression parsing, sorting algorithms, and database indexing.

Key characteristics of binary trees include:
- **Root Node:** The topmost node in the tree.
- **Leaf Nodes:** Nodes that do not have any children.
- **Internal Nodes:** Nodes with at least one child.
- **Subtrees:** A tree consisting of a node and its descendants.

![Binary Tree - visual representation](/DataStructures/BinaryTree/res/binary_tree_visualization.png)

By visualizing the tree structure, it becomes evident how data flows and how operations like insertion, deletion, and traversal are performed. For instance, in a binary search tree (BST), the left child contains nodes with values less than the parent node, and the right child contains nodes with values greater than the parent node. This property enables efficient searching and sorting.

## Implementation
Below is a Python implementation of a balanced binary tree,designed to show how this data structure works. In the next paragraph we will see an implementation that solves a real problem using this structure.

The *Node* class represents each node in the tree with data, left, and right attributes. The *insert* method systematically adds new nodes to maintain optimal balance within the tree after each insertion.

```python
# Define a class for the nodes of the binary tree
class Node:
    def __init__(self, data):
        # Initialize the node with the provided data
        self.data = data
        # Initialize left and right children as None
        self.left = None
        self.right = None

# Define a class for the binary tree
class BinaryTree:
    def __init__(self):
        # Initialize the root of the binary tree as None
        self.root = None
        # Queue to keep track of nodes with available spots
        self.nodes_with_space = []

    def insert(self, data):
        """Insert data into the binary tree to keep it balanced.
        Data is inserted to the right of the last free node if the spot is free,
        otherwise to the left.
        This method is optimized to avoid traversing the tree at each insertion.
        """
        new_node = Node(data)
        # If the tree is empty, set the new node as the root
        if not self.root:
            self.root = new_node
            # Add root to the queue as it may receive children in future insertions
            self.nodes_with_space.append(self.root)
            return

        # Get the first node from the queue that has space
        parent = self.nodes_with_space[0]

        # Insert the new node to the right if it's free
        if not parent.right:
            parent.right = new_node
        # Otherwise, insert to the left
        elif not parent.left:
            parent.left = new_node
            # After both children are filled, remove the parent from the queue
            self.nodes_with_space.pop(0)
        else:
            # This should not happen as we manage the queue accordingly
            pass

        # Add the new node to the queue as it may receive children in future insertions
        self.nodes_with_space.append(new_node)

    def print_tree(self):
        """Print the binary tree level by level with proper indentation to represent its structure.
        All elements at the same level are printed on the same line.
        """
        if not self.root:
            print("Tree is empty.")
            return

        # Get the maximum depth of the tree
        max_level = self.get_max_level(self.root)
        # Start with the root node in the list
        nodes = [self.root]
        # Iterate over each level
        for level in range(1, max_level + 1):
            # Calculate the number of spaces before the first node and between nodes
            spaces_before = ' ' * (2 ** (max_level - level) - 1)
            spaces_between = ' ' * (2 ** (max_level - level + 1) - 1)
            # Print initial spaces
            print(spaces_before, end='')
            # Prepare the list for the next level
            next_level_nodes = []
            # Iterate over the nodes in the current level
            for node in nodes:
                # Print the node's data or a space if the node is None
                if node:
                    print(f'{node.data}', end='')
                    next_level_nodes.append(node.left)
                    next_level_nodes.append(node.right)
                else:
                    print(' ', end='')
                    next_level_nodes.append(None)
                    next_level_nodes.append(None)
                # Print spaces between nodes
                print(spaces_between, end='')
            print()  # Move to the next line after printing all nodes at the current level
            nodes = next_level_nodes  # Move to the next level

    def get_max_level(self, node):
        """Recursively get the maximum depth of the tree."""
        if not node:
            return 0
        left_depth = self.get_max_level(node.left)
        right_depth = self.get_max_level(node.right)
        return max(left_depth, right_depth) + 1

# Example usage
if __name__ == "__main__":
    # Create an instance of BinaryTree
    tree = BinaryTree()
    # List of elements to insert into the tree
    elements = [1, 2, 3, 4, 5, 6, 7, 8]
    for elem in elements:
        tree.insert(elem)
    # Print the binary tree
    tree.print_tree()


```

## The Binary Search Tree
A Binary Search Tree (BST) is a type of binary tree where each node has a comparable key (and associated value) and satisfies the following properties:

Binary Tree Property: Each node has at most two children, referred to as the left child and the right child.
Binary Search Property:
1. The key in the left subtree of a node is less than the key in its parent node.
2. The key in the right subtree of a node is greater than the key in its parent node.
3. Both the left and right subtrees must also be binary search trees.

These properties enable efficient search, insertion, and deletion operations. On average, these operations can be performed in O(log n) time, where n is the number of nodes in the tree, assuming the tree is balanced.

This is a minimal implementation of a BST in Python, including the key operations: insertion, search, and in-order traversal.

```python
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

```
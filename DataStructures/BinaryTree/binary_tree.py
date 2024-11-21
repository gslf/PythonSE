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


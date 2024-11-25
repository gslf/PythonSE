class Node:
    """
    Represents a node in the Red-Black Tree.
    Each node has a key, a color (either "red" or "black"), and pointers to its
    left child, right child, and parent.
    """
    def __init__(self, key, color="red"):
        self.key = key  # The value stored in the node
        self.color = color  # The color of the node ("red" or "black")
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.parent = None  # Pointer to the parent node


class RedBlackTree:
    """
    Represents a Red-Black Tree, a type of self-balancing binary search tree.
    Ensures that the tree remains balanced through specific properties:
    - Every node is either red or black.
    - The root is always black.
    - Red nodes cannot have red children (no two consecutive red nodes).
    - Every path from a node to its descendant null leaves has the same number of black nodes.
    """

    def __init__(self):
        # Sentinel node representing null leaves; always black
        self.TNULL = Node(None, color="black")
        self.root = self.TNULL  # Initially, the tree is empty with only the sentinel node

    def insert(self, key):
        """
        Inserts a new node with the given key into the Red-Black Tree.
        Maintains the binary search tree property and fixes Red-Black properties if violated.
        """
        # Create a new node with the key and default red color
        new_node = Node(key)
        new_node.left = self.TNULL  # New nodes' children are initially TNULL
        new_node.right = self.TNULL

        # Perform standard binary search tree insertion
        parent = None
        current = self.root
        while current != self.TNULL:  # Traverse until reaching a TNULL node
            parent = current
            if key < current.key:  # Traverse left for smaller keys
                current = current.left
            else:  # Traverse right for larger keys
                current = current.right

        # Set the parent of the new node and insert it
        new_node.parent = parent
        if not parent:  # If the tree was empty, set the new node as the root
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # Restore Red-Black Tree properties after insertion
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        """
        Fixes violations of Red-Black Tree properties caused by insertion.
        Ensures the tree remains balanced and adheres to the Red-Black rules.
        """
        while node != self.root and node.parent.color == "red":
            if node.parent == node.parent.parent.left:  # Parent is the left child
                uncle = node.parent.parent.right  # The sibling of the parent (uncle)
                if uncle.color == "red":  # Case 1: Uncle is red
                    uncle.color = "black"
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent  # Move up the tree
                else:
                    if node == node.parent.right:  # Case 2: Node is a right child
                        node = node.parent
                        self._rotate_left(node)  # Perform left rotation
                    # Case 3: Node is a left child
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_right(node.parent.parent)  # Perform right rotation
            else:  # Parent is the right child (mirror cases)
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    uncle.color = "black"
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)  # Perform right rotation
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_left(node.parent.parent)  # Perform left rotation

        # Ensure the root is always black
        self.root.color = "black"

    def _rotate_left(self, node):
        """
        Performs a left rotation on the given node.
        Updates parent and child pointers accordingly.
        """
        right_child = node.right  # The right child becomes the new root of the subtree
        node.right = right_child.left  # Reassign left subtree of right_child
        if right_child.left != self.TNULL:
            right_child.left.parent = node
        right_child.parent = node.parent  # Update parent of the rotated node
        if not node.parent:  # If node was the root
            self.root = right_child
        elif node == node.parent.left:  # Update the parent's child pointer
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node):
        """
        Performs a right rotation on the given node.
        Updates parent and child pointers accordingly.
        """
        left_child = node.left  # The left child becomes the new root of the subtree
        node.left = left_child.right  # Reassign right subtree of left_child
        if left_child.right != self.TNULL:
            left_child.right.parent = node
        left_child.parent = node.parent  # Update parent of the rotated node
        if not node.parent:  # If node was the root
            self.root = left_child
        elif node == node.parent.right:  # Update the parent's child pointer
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

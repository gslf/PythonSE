class Node:
    """
    A class representing a Node in a linked list.
    Attributes:
        data (any): The data stored in the node.
        next_node (Node or None): The reference to the next node in the list.
    """
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"Node({self.data})"


class SinglyLinkedList:
    """
    A class representing a singly linked list.
    Attributes:
        head (Node or None): The first node in the linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append a new node with the provided data to the end of the linked list.
        Args:
            data (any): The data to be added to the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node

    def prepend(self, data):
        """
        Prepend a new node with the provided data to the start of the linked list.
        Args:
            data (any): The data to be added to the list.
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete_value(self, value):
        """
        Delete the first node containing the specified value.
        Args:
            value (any): The value to be deleted from the list.
        """
        if not self.head:
            return

        # If the node to be deleted is the head
        if self.head.data == value:
            self.head = self.head.next_node
            return

        current = self.head
        while current.next_node:
            if current.next_node.data == value:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

    def find(self, value):
        """
        Find a node containing the specified value.
        Args:
            value (any): The value to be found.
        Returns:
            Node or None: The node containing the value, or None if not found.
        """
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next_node
        return None

    def __repr__(self):
        """
        Return a string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next_node
        return " -> ".join(nodes) + " -> None"


# Example usage
if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(3)
    singly_linked_list.append(5)
    singly_linked_list.append(7)
    singly_linked_list.prepend(1)
    print(singly_linked_list)  # Output: Node(1) -> Node(3) -> Node(5) -> Node(7) -> None
    singly_linked_list.delete_value(5)
    print(singly_linked_list)  # Output: Node(1) -> Node(3) -> Node(7) -> None
    print(singly_linked_list.find(7))  # Output: Node(7)
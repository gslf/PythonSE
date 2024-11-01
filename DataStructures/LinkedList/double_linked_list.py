class DoublyNode:
    """
    A class representing a Node in a doubly linked list.
    Attributes:
        data (any): The data stored in the node.
        next_node (DoublyNode or None): The reference to the next node in the list.
        prev_node (DoublyNode or None): The reference to the previous node in the list.
    """
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

    def __repr__(self):
        return f"DoublyNode({self.data})"


class DoublyLinkedList:
    """
    A class representing a doubly linked list.
    Attributes:
        head (DoublyNode or None): The first node in the linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append a new node with the provided data to the end of the doubly linked list.
        Args:
            data (any): The data to be added to the list.
        """
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node
        new_node.prev_node = current

    def prepend(self, data):
        """
        Prepend a new node with the provided data to the start of the doubly linked list.
        Args:
            data (any): The data to be added to the list.
        """
        new_node = DoublyNode(data)
        if self.head:
            self.head.prev_node = new_node
        new_node.next_node = self.head
        self.head = new_node

    def delete_value(self, value):
        """
        Delete the first node containing the specified value from the doubly linked list.
        Args:
            value (any): The value to be deleted from the list.
        """
        if not self.head:
            return

        current = self.head
        while current:
            if current.data == value:
                if current.prev_node:
                    current.prev_node.next_node = current.next_node
                if current.next_node:
                    current.next_node.prev_node = current.prev_node
                if current == self.head:
                    self.head = current.next_node
                return
            current = current.next_node

    def __repr__(self):
        """
        Return a string representation of the doubly linked list.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next_node
        return " <-> ".join(nodes) + " <-> None"


# Example usage
if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(3)
    doubly_linked_list.append(5)
    doubly_linked_list.append(7)
    doubly_linked_list.prepend(1)
    print(doubly_linked_list)  # Output: DoublyNode(1) <-> DoublyNode(3) <-> DoublyNode(5) <-> DoublyNode(7) <-> None
    doubly_linked_list.delete_value(5)
    print(doubly_linked_list)  # Output: DoublyNode(1) <-> DoublyNode(3) <-> DoublyNode(7) <-> None
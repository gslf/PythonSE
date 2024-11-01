class CircularNode:
    """
    A class representing a Node in a circular linked list.
    Attributes:
        data (any): The data stored in the node.
        next_node (CircularNode or None): The reference to the next node in the list.
    """
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"CircularNode({self.data})"


class CircularLinkedList:
    """
    A class representing a circular linked list.
    Attributes:
        head (CircularNode or None): The first node in the circular linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append a new node with the provided data to the circular linked list.
        Args:
            data (any): The data to be added to the list.
        """
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            self.head.next_node = self.head
            return

        current = self.head
        while current.next_node != self.head:
            current = current.next_node
        current.next_node = new_node
        new_node.next_node = self.head

    def __repr__(self):
        """
        Return a string representation of the circular linked list.
        """
        nodes = []
        current = self.head
        if not current:
            return "None"

        while True:
            nodes.append(repr(current))
            current = current.next_node
            if current == self.head:
                break
        return " -> ".join(nodes) + " -> Head"


# Example usage
if __name__ == "__main__":
    circular_linked_list = CircularLinkedList()
    circular_linked_list.append(3)
    circular_linked_list.append(5)
    circular_linked_list.append(7)
    circular_linked_list.append(1)
    print(circular_linked_list)  # Output: CircularNode(3) -> CircularNode(5) -> CircularNode(7) -> CircularNode(1) -> Head
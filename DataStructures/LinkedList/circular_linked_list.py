from typing import Any, Optional

class CircularNode:
    """
    Represents a node in a circular linked list.

    Attributes:
        data (Any): The data stored in the node.
        next_node (Optional[CircularNode]): Reference to the next node in the list.
    """
    def __init__(self, data: Any):
        self.data: Any = data
        self.next_node: Optional[CircularNode] = None

    def __repr__(self) -> str:
        return f"CircularNode({self.data})"


class CircularLinkedList:
    """
    Represents a circular linked list.

    Attributes:
        head (Optional[CircularNode]): The first node in the circular linked list, or None if the list is empty.
    """
    def __init__(self) -> None:
        self.head: Optional[CircularNode] = None

    def append(self, data: Any) -> None:
        """
        Appends a new node with the provided data to the circular linked list.

        Args:
            data (Any): The data to be added to the list.
        """
        new_node = CircularNode(data)
        if self.head is None:
            # If the list is empty, the new node points to itself.
            self.head = new_node
            self.head.next_node = self.head
        else:
            # Traverse to the last node and link it to the new node.
            current = self.head
            while current.next_node != self.head:
                current = current.next_node
            current.next_node = new_node
            new_node.next_node = self.head

    def __repr__(self) -> str:
        """
        Returns a string representation of the circular linked list.
        """
        if not self.head:
            return "Empty List"

        nodes = []
        current = self.head
        while True:
            nodes.append(repr(current))
            current = current.next_node
            if current == self.head:
                break
        return " -> ".join(nodes) + " -> Head"

#################
# Example usage #
#################
if __name__ == "__main__":
    circular_linked_list = CircularLinkedList()
    circular_linked_list.append(3)
    circular_linked_list.append(5)
    circular_linked_list.append(7)
    circular_linked_list.append(1)
    print(circular_linked_list)  # Output: CircularNode(3) -> CircularNode(5) -> CircularNode(7) -> CircularNode(1) -> Head
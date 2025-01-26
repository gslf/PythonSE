from typing import Any, Optional

class DoublyNode:
    """
    A class representing a Node in a doubly linked list.

    Attributes:
        data (Any): The data stored in the node.
        next_node (Optional[DoublyNode]): Reference to the next node in the list, or None if it's the last node.
        prev_node (Optional[DoublyNode]): Reference to the previous node in the list, or None if it's the first node.
    """

    def __init__(self, data: Any):
        self.data: Any = data
        self.next_node: Optional[DoublyNode] = None
        self.prev_node: Optional[DoublyNode] = None

    def __repr__(self) -> str:
        return f"DoublyNode({self.data})"


class DoublyLinkedList:
    """
    A class representing a doubly linked list.

    Attributes:
        head (Optional[DoublyNode]): The first node in the linked list, or None if the list is empty.
    """

    def __init__(self) -> None:
        self.head: Optional[DoublyNode] = None

    def append(self, data: Any) -> None:
        """
        Append a new node with the provided data to the end of the doubly linked list.

        Args:
            data (Any): The data to be added to the list.
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

    def prepend(self, data: Any) -> None:
        """
        Prepend a new node with the provided data to the start of the doubly linked list.

        Args:
            data (Any): The data to be added to the list.
        """
        new_node = DoublyNode(data)
        if self.head:
            self.head.prev_node = new_node
        new_node.next_node = self.head
        self.head = new_node

    def delete_value(self, value: Any) -> None:
        """
        Delete the first node containing the specified value from the doubly linked list.

        Args:
            value (Any): The value to be deleted from the list.
        """
        if not self.head:
            return

        current: Optional[DoublyNode] = self.head
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

    def __repr__(self) -> str:
        """
        Return a string representation of the doubly linked list.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next_node
        return " <-> ".join(nodes) + " <-> None"

#################
# Example usage #
#################
if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(3)
    doubly_linked_list.append(5)
    doubly_linked_list.append(7)
    doubly_linked_list.prepend(1)
    print(doubly_linked_list)  # Output: DoublyNode(1) <-> DoublyNode(3) <-> DoublyNode(5) <-> DoublyNode(7) <-> None
    doubly_linked_list.delete_value(5)
    print(doubly_linked_list)  # Output: DoublyNode(1) <-> DoublyNode(3) <-> DoublyNode(7) <-> None
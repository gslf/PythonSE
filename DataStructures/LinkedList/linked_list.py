from typing import Any, Optional

class Node:
    """
    A class representing a Node in a singly linked list.

    Attributes:
        data (Any): The data stored in the node.
        next_node (Optional[Node]): Reference to the next node in the list, or None if this is the last node.
    """
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next_node: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Optional[Node]): The first node in the linked list, or None if the list is empty.
    """
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def append(self, data: Any) -> None:
        """
        Append a new node with the provided data to the end of the linked list.

        Args:
            data (Any): The data to be added to the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node

    def prepend(self, data: Any) -> None:
        """
        Prepend a new node with the provided data to the start of the linked list.

        Args:
            data (Any): The data to be added to the list.
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete_value(self, value: Any) -> None:
        """
        Delete the first node containing the specified value.

        Args:
            value (Any): The value to be deleted from the list.
        """
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next_node
            return

        current = self.head
        while current.next_node:
            if current.next_node.data == value:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

    def find(self, value: Any) -> Optional[Node]:
        """
        Find a node containing the specified value.

        Args:
            value (Any): The value to be found.

        Returns:
            Optional[Node]: The node containing the value, or None if not found.
        """
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next_node
        return None

    def __repr__(self) -> str:
        """
        Return a string representation of the linked list.

        Example:
            "Node(1) -> Node(3) -> Node(5) -> None"
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
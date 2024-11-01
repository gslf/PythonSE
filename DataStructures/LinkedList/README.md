# Linked lists in Python

A linked list is a linear data structure where elements, called nodes, are linked using pointers. Each node contains two elements: the data and a reference (or pointer) to the next node in the sequence. The linked list starts from a "head" node, and each subsequent node points to the next, until a node points to None, marking the end of the list.

Linked lists come in different types:
- Singly Linked List: Each node points to the next.
- Doubly Linked List: Each node points both to the next and to the previous.
- Circular Linked List: The last node points back to the head.


![Linked List - visual representation](/DataStructures/LinkedList/res/linked_list_visualization.png)

A linked list is like a train with each wagon holding a passenger and having a hook at the back for attaching the next wagon. The head of the linked list is like the locomotive. Each wagon (node) contains the payload (data) and a hook to attach the next wagon (next pointer). You can add a new wagon at any position without needing to rearrange the entire train, and removing a wagon is straightforward—it involves simply detaching it and reconnecting the adjacent wagons. 

## Implementation
Here is an implementation of a simple linked list:
```python
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
```

This is the implementation of a double linked list:
```python
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
```

Here the implementation of a circular linked list
```python
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
```
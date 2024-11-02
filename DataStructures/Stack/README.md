# Stacks in Python

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. It can be thought of as a a tube that holds tennis balls. Each time you place a ball into the tube, it goes on top of the previous one. When you want to remove a ball, the only one you can access is the last one that was added—the ball on the top.

![Stack - visual representation](/DataStructures/Stack/res/stack_visualization.png)

Common Operations on a Stack:
- Push: Adding an element to the top of the stack.
- Pop: Removing the top element from the stack.
- Peek: Viewing the top element without removing it.
- IsEmpty: Checking if the stack has any elements.

Stacks are commonly used in scenarios like parsing expressions, managing function calls (think recursion), and implementing undo mechanisms in software.

## Implementation

In Python, stacks can be implemented in a number of ways, including using lists or the collections.deque class. Here is a self-explainatory implementation:

```python
class Stack:
    def __init__(self):
        """
        Initializes an empty stack.
        """
        self._items = []

    def push(self, item):
        """
        Adds an item to the top of the stack.
        :param item: Item to be added to the stack.
        """
        self._items.append(item)

    def pop(self):
        """
        Removes and returns the item from the top of the stack.
        :return: The top item of the stack.
        :raises IndexError: If the stack is empty when trying to pop.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """
        Returns the item from the top of the stack without removing it.
        :return: The top item of the stack.
        :raises IndexError: If the stack is empty when trying to peek.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self._items[-1]

    def is_empty(self):
        """
        Checks if the stack is empty.
        :return: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0

    def size(self):
        """
        Returns the number of items in the stack.
        :return: The size of the stack.
        """
        return len(self._items)

# Example usage
if __name__ == "__main__":
    print("Create a new stack")
    stack = Stack()

    print("Push 'A', 'B', and 'C' in the stack")
    stack.push("A")
    stack.push("B")
    stack.push("C")
    
    print(f"Top item: {stack.peek()}")  # Output: Top item: C
    print(f"Stack size: {stack.size()}")  # Output: Stack size: 3
    stack.pop()
    print(f"Top item after pop: {stack.peek()}")  # Output: Top item after pop: B
```
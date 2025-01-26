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

#################
# Example usage #
#################
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
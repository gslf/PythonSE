class StandardQueue:
    def __init__(self):
        from collections import deque
        self.queue = deque()

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue.")
        return self.queue.popleft()

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue.")
        return self.queue[0]

# Example usage: 
my_queue = StandardQueue()

print("Enqueue A B C")
my_queue.enqueue("A"); 
my_queue.enqueue("B"); 
my_queue.enqueue("C")


print(f"Dequeue: {my_queue.dequeue()}")  # Dequeue: "A"
print(f"Empty? {my_queue.is_empty()}")  # Empty False
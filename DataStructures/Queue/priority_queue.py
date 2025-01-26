class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        """Add an item to the queue with the given priority."""
        self.queue.append((priority, item))
        self.queue.sort(key=lambda x: x[0])  # Keep the queue sorted by priority (lowest first)

    def dequeue(self):
        """Remove and return the item with the highest priority."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue.")
        return self.queue.pop(0)[1]  # Remove and return the item with the lowest priority value

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

##################
# Example usage: # 
##################
my_queue = PriorityQueue()
my_queue.enqueue('A', 2)
my_queue.enqueue('B', 1)
my_queue.enqueue('C', 1)

print(f"Dequeue: {my_queue.dequeue()}")  # Dequeue: "B"
print(f"Empty? {my_queue.is_empty()}")  # Empty False
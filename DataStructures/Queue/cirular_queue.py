class CircularQueue:
    def __init__(self, capacity):
        """Initialize the queue with a fixed capacity."""
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        """Add an item to the next available position."""
        if self.size == self.capacity:
            raise OverflowError("Queue is full.")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue.")
        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear the slot
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.size == self.capacity
    
##################
# Example usage: # 
##################
my_queue = CircularQueue(3)
my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')

print(f"Full? {my_queue.is_full()}")  # Full? Trye
print(f"Dequeue: {my_queue.dequeue()}")  # Dequeue: "B"
print(f"Full? {my_queue.is_full()}")  # Full? False
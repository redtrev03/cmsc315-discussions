"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

A Stack follows Last-In, First-Out (LIFO), meaning the most
recently added item is the first item removed.

A Queue follows First-In, First-Out (FIFO), meaning the first
item added is the first item removed.
"""

from collections import deque


class Stack:
    def __init__(self):
        # A Python list stores the values in the stack.
        self.items = []

    def push(self, value):
        # Adding to the end makes this value the new "top,"
        # supporting Last-In, First-Out (LIFO) behavior.
        self.items.append(value)

    def pop(self):
        # Check for an empty stack before trying to remove an item.
        if self.is_empty():
            return None

        # Remove and return the most recently added item.
        return self.items.pop()

    def peek(self):
        # Peek returns the top item without removing it.
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        # Return True when the stack contains no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # A deque is efficient for adding to the back and
        # removing items from the front of the queue.
        self.items = deque()

    def enqueue(self, value):
        # Adding to the back ensures earlier values remain at
        # the front, supporting First-In, First-Out (FIFO).
        self.items.append(value)

    def dequeue(self):
        # Check for an empty queue before trying to remove an item.
        if self.is_empty():
            return None

        # Remove and return the value at the front of the queue.
        return self.items.popleft()

    def front(self):
        # Front returns the first value without removing it.
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        # Return True when the queue contains no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")

    stack = Stack()

    print("Adding four values to the stack: 10, 20, 30, and 40")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print("Current stack:", stack.items)
    print("The top value is:", stack.peek())

    # Demonstrate LIFO behavior.
    print("\nDemonstrating LIFO behavior:")
    print("First pop:", stack.pop())
    print("Second pop:", stack.pop())
    print("Third pop:", stack.pop())
    print("Fourth pop:", stack.pop())

    print("Is the stack empty?", stack.is_empty())

    # Test popping from an empty stack.
    print("\nAttempting to pop from an empty stack:")
    print("Result:", stack.pop())

    # Test peeking at an empty stack.
    print("\nAttempting to peek at an empty stack:")
    print("Result:", stack.peek())

    # Test a stack containing only one item.
    print("\nTesting a single-item stack:")
    single_stack = Stack()
    single_stack.push("Only Item")

    print("Added:", single_stack.peek())
    print("Removed:", single_stack.pop())
    print("Is the single-item stack now empty?", single_stack.is_empty())

    # ===============================
    # QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    print("Adding four values to the queue: A, B, C, and D")
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.enqueue("D")

    print("Current queue:", list(queue.items))
    print("The front value is:", queue.front())

    # Demonstrate FIFO behavior.
    print("\nDemonstrating FIFO behavior:")
    print("First dequeue:", queue.dequeue())
    print("Second dequeue:", queue.dequeue())
    print("Third dequeue:", queue.dequeue())
    print("Fourth dequeue:", queue.dequeue())

    print("Is the queue empty?", queue.is_empty())

    # Test dequeuing from an empty queue.
    print("\nAttempting to dequeue from an empty queue:")
    print("Result:", queue.dequeue())

    # Test viewing the front of an empty queue.
    print("\nAttempting to view the front of an empty queue:")
    print("Result:", queue.front())

    # Test a queue containing only one item.
    print("\nTesting a single-item queue:")
    single_queue = Queue()
    single_queue.enqueue("Only Item")

    print("Added:", single_queue.front())
    print("Removed:", single_queue.dequeue())
    print("Is the single-item queue now empty?", single_queue.is_empty())


if __name__ == "__main__":
    main()
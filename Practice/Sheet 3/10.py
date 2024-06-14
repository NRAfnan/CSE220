class Node:
    def __init__(self, elem, nxt):
        self.elem = elem
        self.next = nxt


class Queue:
    def __init__(self):
        self.front = None
        self.back = self.front

    def enqueue(self, obj):
        if self.front is None:
            node = Node(obj, None)
            self.front = node
            self.back = self.front
        else:
            node = Node(obj, None)
            self.back.next = node
            self.back = self.back.next

    def dequeue(self):
        if self.front is None:
            print("Underflow!!")
        else:
            dequeued = self.front.elem
            self.front = self.front.next
            return dequeued

    def peek(self):
        if self.front is None:
            print("Underflow!!")
        else:
            return self.front.elem

    def is_empty(self):
        return self.front is None


class QueueWithDummyHead:
    def __init__(self):
        self.front = Node("Dummy head", None)
        self.back = self.front

    def enqueue(self, obj):
        if self.front.next is None:
            node = Node(obj, None)
            self.front.next = node
            self.back = self.front.next
        else:
            node = Node(obj, None)
            self.back.next = node
            self.back = self.back.next

    def dequeue(self):
        if self.front.next is None:
            print("Underflow!!")
        else:
            dequeued = self.front.next.elem
            self.front.next = self.front.next.next
            return dequeued

    def peek(self):
        if self.front.next is None:
            print("Underflow!!")
        else:
            return self.front.next.elem

    def is_empty(self):
        return self.front.next is None


# Test the QueueWithDummyHead class
queue = QueueWithDummyHead()

# Test is_empty
print("Is queue empty?", queue.is_empty())  # Should print True

# Test enqueue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Test peek
print("Peeked element:", queue.peek())  # Should peek at 1

# Test dequeue
print("Dequeued element:", queue.dequeue())  # Should dequeue 1
print("Dequeued element:", queue.dequeue())  # Should dequeue 2
print("Dequeued element:", queue.dequeue())  # Should dequeue 3

# Test is_empty
print("Is queue empty?", queue.is_empty())  # Should print True

# Test peek
queue.enqueue(4)
print("Peeked element:", queue.peek())  # Should peek at 4

# Test is_empty
print("Is queue empty?", queue.is_empty())  # Should print False

# Test dequeue on empty queue
print("Dequeued element:", queue.dequeue())  # Should dequeue 4

# Test dequeue on empty queue
print("Dequeued element:", queue.dequeue())  # Should print Underflow!!
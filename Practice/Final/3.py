class Queue:
    def __init__(self, c):
        self.cA = [None] * c
        self.front = c - 1
        self.back = c - 1

    def enqueue(self, item):
        if self.front == self.back and self.cA[self.front] is not None:
            print("Queue Overflow")
        self.cA[self.back] = item
        self.back = (self.back + 1) % len(self.cA)

    def dequeue(self):
        if self.front == self.back and self.cA[self.front] is None:
            print("Queue Underflow")
        dequeued = self.cA[self.front]
        self.cA[self.front] = None
        self.front = (self.front + 1) % len(self.cA)

    def peek(self):
        if self.front == self.back and self.cA[self.front] is None:
            print("Queue Underflow")
        return self.cA[self.front]

    def is_empty(self):
        return self.front == self.back and self.cA[self.front] is None


def test(arr, queue):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            queue.enqueue(arr[i])
        else:
            queue.dequeue()
        print(queue.cA)
        print(queue.front)
        print(queue.back)


que = Queue(4)
arr = [10, 20, 31, 40, 53]
test(arr, que)
print((67+7+66) % 3)

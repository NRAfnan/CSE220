class Queue:
    def __init__(self):
        self.queue = [None] * 5
        self.size = 0
        self.front = 0
        self.back = 0

    def enqueue(self, obj):
        if self.size == len(self.queue):
            print("Overflow!!")
        else:
            self.queue[self.back] = obj
            self.back = (self.back + 1) % len(self.queue)
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Underflow!!")
        else:
            dequeued = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % len(self.queue)
            self.size -= 1
            return dequeued

    def peek(self):
        if self.size == 0:
            print("Underflow!!")
        else:
            return self.queue[self.front]

    def is_empty(self):
        return self.size == 0


que1 = Queue()
for i in range(5):
    print(que1.back)
    que1.enqueue(i)
print(que1.back)
que1.enqueue(6)
print(que1.peek())
print("========")
for i in range(5):
    print(que1.front)
    print("dequeued:", que1.dequeue())
    print("peeked:", que1.peek())
print(que1.front)
que1.dequeue()
print("====")
que1.enqueue(6)
que1.enqueue(7)
que1.enqueue(8)
que1.enqueue(9)
que1.enqueue(10)
for i in range(5):
    print("front", que1.front)
    print("dequeued:", que1.dequeue())
    print("Updated front", que1.front)
    print("peeked:", que1.peek())
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


def bill_exchange(bills):
    bills_queue = Queue()
    for bill in bills:
        bills_queue.enqueue(bill)

    exchange_queue = Queue()
    for bill in bills:
        if bill == 5:
            exchange_queue.enqueue(bill)
            bills_queue.dequeue()
        else:
            temp_exchange = 0
            while not exchange_queue.is_empty():
                temp_exchange += exchange_queue.dequeue()
                if bill - temp_exchange == 5:
                    exchange_queue.enqueue(bill)
                    bills_queue.dequeue()
                    break
    return bills_queue.is_empty()


print(bill_exchange([5, 5, 5, 10, 20]))
class Node:
    def __init__(self, elem, nxt):
        self.elem = elem
        self.next = nxt


class Stack:
    def __init__(self):
        self.stack = [None] * 20
        self.size = 0
        self.top = 0

    def push(self, obj):
        if self.size == len(self.stack):
            print("Stack Overflow!!")
        else:
            self.stack[self.top] = obj
            self.top += 1
            self.size += 1

    def pop(self):
        if self.size == 0:
            print("Stack Underflow!!")
        else:
            temp = self.stack[self.top - 1]
            self.stack[self.top - 1] = None
            self.top -= 1
            self.size -= 1
            return temp

    def peek(self):
        if self.size == 0:
            print("Stack Underflow!!")
        else:
            return self.stack[self.top - 1]

    def is_empty(self):
        return self.size == 0


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
            print("Queue Underflow!!")
        else:
            elem = self.front.elem
            self.front = self.front.next
            return elem

    def peek(self):
        if self.front is None:
            return None
        return self.front.elem

    def is_empty(self):
        return self.front is None


def get_sandwiches(st, sd):
    stack_sd = Stack()
    j = len(sd) - 1
    while j >= 0:
        stack_sd.push(sd[j])
        j -= 1

    number_of_students = len(st)
    queue_st = Queue()
    i = 0
    while i < number_of_students:
        queue_st.enqueue(st[i])
        i += 1

    """
    if we make all the students go back of the line then we break the loop
    if 1 student prefers a sandwich then and the sandwich stacks get updated then it is as if the queue again starts from 0
    so we set count to 0
    """
    count = 0
    while count < number_of_students:
        if stack_sd.peek() == queue_st.peek():
            stack_sd.pop()
            queue_st.dequeue()
            number_of_students -= 1
            count = 0
        else:
            going_back_to_the_line = queue_st.dequeue()
            queue_st.enqueue(going_back_to_the_line)
            count += 1
    return number_of_students


print(get_sandwiches([1, 1, 0, 0], [0, 1, 0, 1]))
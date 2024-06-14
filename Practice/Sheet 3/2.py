class Node:
    def __init__(self, elem, nxt):
        self.elem = elem
        self.next = nxt


class Stack:
    def __init__(self):
        self.__top = None

    def push(self, obj):
        node = Node(obj, self.__top)
        self.__top = node

    def pop(self):
        if self.__top is not None:
            popped = self.__top.elem
            self.__top = self.__top.next
            return popped
        else:
            print("Underflow!!")

    def peek(self):
        if self.__top is not None:
            return self.__top.elem
        else:
            print("Underflow")

    def is_empty(self):
        return self.__top is None
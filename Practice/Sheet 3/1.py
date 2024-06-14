class Stack:
    def __init__(self):
        self.stack = [None] * 20
        self.__top = 0
        self.__size = 0

    def push(self, obj):
        if self.__size == len(self.stack):
            print("Overflow!!")
        else:
            self.stack[self.__top] = obj
            self.__top += 1
            self.__size += 1

    def pop(self):
        if self.__size == 0:
            print("Underflow!!")
        else:
            popped = self.stack[self.__top - 1]
            self.stack[self.__top - 1] = None
            self.__top -= 1
            self.__size -= 1
            return popped

    def peek(self):
        if self.__size == 0:
            print("Underflow!!")
        else:
            return self.stack[self.__top - 1]

    def is_empty(self):
        return self.__size == 0
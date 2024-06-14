class Stack:
    def __init__(self):
        self.stack = [None] * 20
        self.top = 0
        self.size = 0

    def push(self, obj):
        if self.size == len(self.stack):
            print("Stack Overflow!!!")
        else:
            self.stack[self.top] = obj
            self.top += 1
            self.size += 1

    def pop(self):
        if self.size == 0:
            print("Stack Underflow!!!")
        else:
            temp = self.stack[self.top - 1]
            self.stack[self.top - 1] = None
            self.top -= 1
            self.size -= 1
            return temp

    def peek(self):
        if self.size == 0:
            print("Stack Underflow!!!")
        else:
            return self.stack[self.top - 1]


def rev_using_stack(given_str):
    stack = Stack()
    i = 0
    while i < len(given_str):
        stack.push(given_str[i])
        i += 1

    str1 = ""
    j = 0
    while j < len(given_str):
        str1 += stack.pop()
        j += 1

    return str1


print(rev_using_stack("CSE220"))
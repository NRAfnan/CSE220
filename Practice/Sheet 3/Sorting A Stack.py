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


def sort_stack(stack):
    """
    Ascending order
    1. Initialize a temp stack
    2. If the temp stack is empty push number
    3. If top is not empty compare top with the number that we want to push
    4. If top is greater pop top push lesser number and push top
    5. Otherwise, push number
    :param stack: Stack
    :return: Sorted Stack
    """
    temp_stack = Stack()
    while not stack.is_empty():
        popped = stack.pop()
        if temp_stack.is_empty():
            temp_stack.push(popped)
        elif temp_stack.peek() < popped:
            temp_stack.push(popped)
        elif temp_stack.peek() > popped:
            compare(popped, temp_stack)

    return temp_stack


def compare(num, stack):
    if not stack.is_empty() and stack.peek() > num:
        temp = stack.pop()
        compare(num, stack)
        return stack.push(temp)
    else:
        return stack.push(num)


def print_stack(st):
    if st.is_empty():
        return
    p = st.pop()
    print('|', p, "|")
    print_stack(st)
    st.push(p)


stack1 = Stack()
list1 = [1, 5, 4, 2, 3]
for i in list1:
    stack1.push(i)
print_stack(stack1)
print("=========")
stack2 = sort_stack(stack1)
print_stack(stack2)

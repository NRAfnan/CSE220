class Node:
    def __init__(self, elem=None, next=None):
        self.elem = elem
        self.next = next


class Stack:
    def __init__(self):
        self.__top = None

    def push(self, elem):
        nn = Node(elem, self.__top)
        self.__top = nn

    def pop(self):
        if self.__top == None:
            # print('Stack Underflow')
            return None
        e = self.__top
        self.__top = self.__top.next
        return e.elem

    def peek(self):
        if self.__top == None:
            # print('Stack Underflow')
            return None
        return self.__top.elem

    def isEmpty(self):
        return self.__top == None


def print_stack(st):
    if st.isEmpty():
        return
    p = st.pop()
    print('|', p, end=' ')
    if p < 10:
        print(' |')
    else:
        print('|')
    # print('------')
    print_stack(st)
    st.push(p)


def conditional_reverse(stack):
    """
    1. Initialize a new stack
    2. We iterate till the last element of given stack
    3. We pop and push when there is no occurrence of consecutive values
    :param stack: Given stack of stack structure of linked list
    :return: new_stack
    """
    new_stack = Stack()
    while not stack.isEmpty():
        popped = stack.pop()
        peeked_ns = new_stack.peek()
        if peeked_ns != popped:
            new_stack.push(popped)
    return new_stack


print('Test 01')
st=Stack()
st.push(10)
st.push(10)
st.push(20)
st.push(20)
st.push(30)
st.push(10)
st.push(50)
print('Stack:')
print_stack(st)
print('------')
reversed_stack=conditional_reverse(st)
print('Conditional Reversed Stack:')
print_stack(reversed_stack)  # This stack contains 50, 10, 30, 20, 10 in this order whereas top element should be 10
print('------')
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


def remove_block(stack, n):
    """
    1. Initialize a temp stack
    2. We pop one item from the original stack and push it to the temp stack to store it
    3. Then we pop the n th element from the given stack
    4. Now, we pop one element from temp stack and push it the original stack
    :param stack: A stack data structure
    :param n: An int corresponding to the index of node we have to remove from top
    :return: Modified given stack
    """
    temp_stack = Stack()
    for i in range(n - 1):
        popped = stack.pop()
        temp_stack.push(popped)

    # in here top is the nth element we need to remove
    stack.pop()

    while not temp_stack.isEmpty():
        popped = temp_stack.pop()
        stack.push(popped)


print('Test 01')
st = Stack()
st.push(4)
st.push(19)
st.push(23)
st.push(17)
st.push(5)
print('Stack:')
print_stack(st)
print('------')
remove_block(st, 2)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()

print('Test 02')
st = Stack()
st.push(73)
st.push(85)
st.push(15)
st.push(41)
print('Stack:')
print_stack(st)
print('------')
remove_block(st, 3)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()

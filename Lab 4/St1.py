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


# def diamond_count(stack, string):
#     """
#     This is wrong. For the following reason.
#     This takes into consideration >< as a diamond, so it pushes both "<" and ">" inside the stack and according to the
#     corresponding opposite bracer pops
#     :param stack:
#     :param string:
#     :return:
#     """
#     count = 0
#     for char in string:
#         if char == "<" or char == ">":
#             peeked_char = stack.peek()
#             if peeked_char is not None:
#                 if peeked_char == "<" and char == ">":
#                     stack.pop()
#                     count += 1
#                     continue
#                 elif peeked_char == ">" and char == "<":
#                     stack.pop()
#                     count += 1
#                     continue
#             stack.push(char)
#     return count


def diamond_count(stack, string):
    """
    1. Initialize count
    2. Iterate diamond string
    3. Push "<" in stack
    4. If char ">" and stack is filled with "<" we pop and increase count
    :param stack: Empty stack of Linked list type
    :param string: A str pf Diamonds
    :return: An int of Diamond count
    """
    count = 0
    for char in string:
        if char == '<':
            stack.push(char)
        elif char == '>' and not stack.isEmpty() and stack.peek() == '<':
            stack.pop()
            count += 1
    return count


print('Test 01')
stack = Stack()
string = '<..><.<..>> '
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
#unittest.output_test(returned_value, 3)
print('-----------------------------------------')


print('Test 02')
stack = Stack()
string = '<<<..<......<<<<....>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 1
#unittest.output_test(returned_value, 1)
print('-----------------------------------------')


print('Test 03')
stack = Stack()
string = '>>><...<<..>>...>...>>>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
#unittest.output_test(returned_value, 3)
print('-----------------------------------------')
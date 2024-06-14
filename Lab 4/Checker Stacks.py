# class Node:
#     def __init__(self, elem=None, next=None):
#         self.elem = elem
#         self.next = next
#
#
# class Stack:
#     def __init__(self):
#         self.__top = None
#
#     def push(self, elem):
#         nn = Node(elem, self.__top)
#         self.__top = nn
#
#     def pop(self):
#         if self.__top == None:
#             # print('Stack Underflow')
#             return None
#         e = self.__top
#         self.__top = self.__top.next
#         return e.elem
#
#     def peek(self):
#         if self.__top == None:
#             # print('Stack Underflow')
#             return None
#         return self.__top.elem
#
#     def isEmpty(self):
#         return self.__top == None
#
#
# def print_stack(st):
#     if st.isEmpty():
#         return
#     p = st.pop()
#     print('|', p, end=' ')
#     if p < 10:
#         print(' |')
#     else:
#         print('|')
#     # print('------')
#     print_stack(st)
#     st.push(p)
#
# st = Stack()
# st.push(4)
# st.push(3)
# st.push(5)
# st.push(1)
# st.push(9)
#
# print('Peeked Element: ',st.peek())
# print('Popped Element: ',st.pop())
# print('Popped Element: ',st.pop())
# print('Popped Element: ',st.pop())
# print('Peeked Element: ',st.peek())
# print('Popped Element: ',st.pop())
# print('Popped Element: ',st.pop())
# print('Peeked Element: ',st.peek())
# print('Popped Element: ',st.pop())
# print(st.isEmpty())
#
# st = Stack()
# st.push(4)
# st.push(3)
# st.push(5)
# st.push(1)
# st.push(9)
# print_stack(st)
# print('------')

patients1 = {"Patient 1": [1, "abc", 34, "B+"],
             "Patient 2": [2, "Gojo", 54, "A+"],
             "Patient 3": [3, "Geto", 24, "B-"]}

patients2 = {"Patient 4": [4, "Tanjiro", 94, "AB+"],
             "Patient 5": [5, "Eren", 14, "A-"],
             "Patient 6": [6, "Naruto", 104, "0-"]}
print(patients1["Patient 1"])
print(patients1["Patient 1"][0])
print(patients1["Patient 1"][1])
print(patients1["Patient 1"][2])
print(patients1["Patient 1"][3])
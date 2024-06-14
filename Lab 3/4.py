import numpy as np


class Node:
    def __init__(self, elem, next=None):
        self.elem, self.next = elem, next


def createList(arr):
    head = Node(arr[0])
    tail = head
    for i in range(1, len(arr)):
        newNode = Node(arr[i])
        tail.next = newNode
        tail = newNode
    return head


def printLinkedList(head):
    temp = head
    while temp != None:
        if temp.next != None:
            print(temp.elem, end='-->')
        else:
            print(temp.elem)
        temp = temp.next
    print()


def word_Decoder(head):
    """
    1. Count the number of Nodes
    2. Get num the multiple of whose indexes we will attach in our new linked list
    3. Create dummy headed node
    4. In the for loop create nodes of corresponding indexes in reverse order
    :param head: A non dummy headed linear singly linked list
    :return: A dummy headed linear singly linked list
    """
    count = count_sll(head)
    num = 13 % count
    dummy_head = Node(None, None)
    last_node_next = None
    for i in range(num, count, num):
        n = node_at(head, i)
        new = Node(n.elem, last_node_next)
        last_node_next = new
    dummy_head.next = last_node_next
    return dummy_head


def node_at(head, idx):
    n = head
    count = 0
    while n is not None:
        if count == idx:
            return n
        count += 1
        n = n.next
    return None


def count_sll(head):
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    return count


# A little efficient
# def word_Decoder(head):
#     """
#     1. Count the number of Nodes
#     2. Get x the multiple of whose indexes we will attach in our new linked list
#     3. Create dummy headed node
#     4. In the for loop create nodes of corresponding indexes in reverse order
#     :param head: A non dummy headed linear singly linked list
#     :return: A dummy headed linear singly linked list
#     """
#     count = 0
#     temp = head
#     while temp != None:
#         count += 1
#         temp = temp.next
#     x = 13 % count
#     dummy_head = Node(None, None)
#     last_node_next = None
#     for i in range(x, count, x):
#         n = node_at(head, i)
#         new = Node(n.elem, last_node_next)
#         last_node_next = new
#     dummy_head.next = last_node_next
#     return dummy_head


# Driver Code
print('==============Test Case 1=============')
head = createList(np.array(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C']))
print("Encoded Word:")
printLinkedList(head)  # This should print B→M→D→T→N→O→A→P→S→C

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)  # This should print None→C→A→T

print('==============Test Case 2=============')

head = createList(np.array(['Z', 'O', 'T', 'N', 'X']))
print("Encoded Word:")
printLinkedList(head)  # This should print Z→O→T→N→X

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)  # This should print None→N

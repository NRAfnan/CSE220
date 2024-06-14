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


def sum_dist(head, arr):
    """
    1. Traverse arr
    2. For each number in arr us the number as index to get the corresponding linked list elem
    3. If it is not None then sum it to result
    :param head:
    :param arr:
    :return: An, int Sum of results
    """
    i = 0
    result = 0
    while i < len(arr):
        n = node_at(head, arr[i])
        if n is not None:
            result += n.elem
        i += 1
    return result


def node_at(head, idx):
    n = head
    count = 0
    while n is not None:
        if count == idx:
            return n
        count += 1
        n = n.next
    return None



print('==============Test Case 1=============')
LL1 = createList(np.array([10,16,-5,9,3,4]))
dist = np.array([2,0,5,2,8])
returned_value = sum_dist(LL1, dist)
print(f'Sum of Nodes: {returned_value}') #This should print Sum of Nodes: 4
print()
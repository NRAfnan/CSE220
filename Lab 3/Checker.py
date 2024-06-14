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


def idGenerator(head1, head2, head3):
    """
    1. Initialize new output linked list
    2. Reverse head1 LL
    3. Traverse both head2 and head3 and sum the elements
    4. Add them in output linked list if they between 0 <= <= 9
    5. If otherwise, sum the mod by 10 and then add to output LL
    :param head1: A non dummy headed linear singly linked list
    :param head2: A non dummy headed linear singly linked list
    :param head3: A non dummy headed linear singly linked list
    :return: A new modified linked list
    """
    output_linked_list = reverse_out_of_place(head1)
    print("loc",head2)
    while head2 is not None:
        print(head2.elem)
        head2 = head2.next
    print("loc",head2)


def reverse_out_of_place(head):
    n = Node(head.elem, None)
    temp = head.next
    while temp is not None:
        n = Node(temp.elem, n)
        temp = temp.next
    return n

print('==============Test Case 1=============')
head1 = createList(np.array([0,3,2,2]))
head2 = createList(np.array([5,2,2,1]))
head3 = createList(np.array([4,3,2,1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print  2 → 2 → 3 → 0 → 9 → 5 → 4 → 2
print("=====")
print(head2)
printLinkedList(head2)
print("=====")
while head2 is not None:
    print(head2.elem)
    head2 = head2.next
print(head2)
print("===")
printLinkedList(head2)
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


def alternate_merge(head1, head2):
    """
    Note - We are creating copy of the objects otherwise, both head1 and head2 gets messed up
    1. Initialize temp1, temp2
    2. Initialize modified_linked_list as head1s head as the head
    3. Initialize i = 0
    4. Traverse until both head1 or head2 linked list is finished
    5. If i % 2 == 0 (even) add elements of head1 in the modified linked list
    6. If i % 2 == 1 (odd) add elements of head2 in the modified linked list
    :param head1:
    :param head2:
    :return:
    """
    temp1 = head1.next
    temp2 = head2
    modified_linked_list_head = Node(head1.elem, None)
    modified_linked_list_tail = modified_linked_list_head
    i = 1
    while temp1 is not None or temp2 is not None:
        if i % 2 == 0:
            modified_linked_list_tail.next = Node(temp1.elem, None)
            modified_linked_list_tail = modified_linked_list_tail.next
            temp1 = temp1.next
        else:
            modified_linked_list_tail.next = Node(temp2.elem, None)
            modified_linked_list_tail = modified_linked_list_tail.next
            temp2 = temp2.next
        i += 1
    return modified_linked_list_head


print('==============Test Case 1=============')
head1 = createList(np.array([1,2,6,8,11]))
head2 = createList(np.array([5,7,3,9,4]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print    1 --> 5 --> 2 --> 7 --> 6 --> 3 --> 8 --> 9 --> 11 --> 4


print('==============Test Case 2=============')
head1 = createList(np.array([5, 3, 2, -4]))
head2 = createList(np.array([-4, -6, 1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print    5 → -4 -> 3 → -6 -> 2 -> 1 -> -4


print('==============Test Case 3=============')
head1 = createList(np.array([4, 2, -2, -4]))
head2 = createList(np.array([8, 6, 5, -3]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print   4-> 8 → 2-> 6 → -2 → 5 → -4 -> -3
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


def remove_compartment(head,n):
    """
    1. Count the number of nodes(len) in the list
    2. Get the index of the node situated before the removed node which is = (len - n(given)) - 1) [as our linked list indexing starts at 0]
    3. Remove the node considering the two cases
        1. We may need to remove the head
        2. We may need to remove except head
    :param head: A non dummy headed linear singly linked list
    :param n: An int, The indexing from the back of the linked list starting from 1 instead of 0
    :return: Modified linked list with removed node
    """
    linked_list_len = count_sll(head)
    # if head
    if linked_list_len == n:
        removed_node = head
        head = head.next
        # for garbage collection
        removed_node.next = None
        removed_node.elem = None
        removed_node = None
    else:
        idx_predecessor = linked_list_len - n - 1
        if idx_predecessor < 0:
            return head
        predecessor_node = node_at(head, idx_predecessor)
        removed_node = predecessor_node.next
        predecessor_node.next = removed_node.next
        # for garbage collection
        removed_node.next = None
        removed_node.elem = None
        removed_node = None
    return head



def node_at(head, idx):
    count = 0
    n = head
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


# import gc
#
# def remove_compartment(head,n):
#     """
#     1. Count the number of nodes(len) in the list
#     2. Get the index of the node situated before the removed node which is = (len - n(given)) - 1) [as our linked list indexing starts at 0]
#     3. Remove the node considering the two cases
#         1. We may need to remove the head
#         2. We may need to remove except head
#     :param head: A non dummy headed linear singly linked list
#     :param n: An int, The indexing from the back of the linked list starting from 1 instead of 0
#     :return: Modified linked list with removed node
#     """
#     linked_list_len = count_sll(head)
#     # if head
#     if linked_list_len == n:
#         removed_node = head
#         head = head.next
#         removed_node.next = None  # Unlink the removed node
#         del removed_node  # Remove reference to the removed node
#         gc.collect()  # Perform garbage collection
#     else:
#         idx_predecessor = linked_list_len - n - 1
#         if idx_predecessor < 0:
#             return head
#         predecessor_node = node_at(head, idx_predecessor)
#         removed_node = predecessor_node.next
#         predecessor_node.next = removed_node.next
#         removed_node.next = None  # Unlink the removed node
#         del removed_node  # Remove reference to the removed node
#         gc.collect()  # Perform garbage collection
#     return head
"""
In this modified version, after removing the node from the linked list and unlinking it, 
we explicitly call gc.collect() to trigger garbage collection. 
This helps to release the memory associated with the removed node.
"""




print('==============Test Case 1=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,2)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->34-->41-->72
print()
print('==============Test Case 2=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,7)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->34-->41-->56-->72
print()
print('==============Test Case 3=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,6)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 15-->34-->41-->56-->72
print()
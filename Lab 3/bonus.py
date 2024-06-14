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
    temp_h2 = head2
    temp_h3 = head3
    output_linked_list_tail = get_tail_of_ll(output_linked_list)
    while temp_h2 is not None:
        resultant = temp_h2.elem + temp_h3.elem
        if 0 <= resultant <= 9:
            output_linked_list_tail.next = Node(resultant, None)
            output_linked_list_tail = output_linked_list_tail.next
        elif resultant > 9:
            resultant = resultant % 10
            output_linked_list_tail.next = Node(resultant, None)
            output_linked_list_tail = output_linked_list_tail.next
        temp_h2 = temp_h2.next
        temp_h3 = temp_h3.next
    return output_linked_list


def get_tail_of_ll(head):
    tail = head
    while tail.next is not None:
        tail = tail.next
    return tail


def reverse_out_of_place(head):
    new_head = Node(head.elem, None)
    temp = head.next
    while temp is not None:
        n = Node(temp.elem, new_head)
        new_head = n
        temp = temp.next
    return new_head
    # A little efficient
    # n = Node(head.elem, None)
    # temp = head.next
    # while temp is not None:
    #     n = Node(temp.elem, n)
    #     temp = temp.next
    # return n


print('==============Test Case 1=============')
head1 = createList(np.array([0,3,2,2]))
head2 = createList(np.array([5,2,2,1]))
head3 = createList(np.array([4,3,2,1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print  2 → 2 → 3 → 0 → 9 → 5 → 4 → 2


print('==============Test Case 2=============')
head1 = createList(np.array([0,3,9,1]))
head2 = createList(np.array([3,6,5,7]))
head3 = createList(np.array([2,4,3,8]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print 1 → 9 → 3 → 0 → 5 → 0 → 8 → 5
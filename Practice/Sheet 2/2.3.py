class Node:
    def __init__(self, data, nxt):
        self.data = data
        self.next = nxt


def create_list(lst):
    head = None
    n = Node(lst[0], None)
    head = n
    tail = head
    i = 1
    while i < len(lst):
        n = Node(lst[i], None)
        tail.next = n
        tail = tail.next
        i += 1
    return head


def iterate_list(head):
    n = head
    while n is not None:
        if n.next is not None:
            print(n.data, end=" ")
        else:
            print(n.data)
        n = n.next


# def subpart_even_reverse(head):
#     """
#     2 cases -
#     1. A subpart starts from the head
#     2. A subpart starts somewhere middle
#     For case 1 - If head is even then we start from and reverse the subpart in place
#     For case 2 - If we find an even number in the middle then we start the reverse
#     :param head:
#     :return:
#     """
#     subpart_head = None
#     subpart_tail = subpart_head
#     subpart_overhead = None
#     n = head
#     while n is not None:
#         if n.next is not None and n.next.data % 2 == 0 and subpart_overhead is None:
#             subpart_overhead = n
#         if subpart_head is None and n.data % 2 == 0 and n.next.data % 2 == 0:
#             subpart_head = n
#             subpart_tail = subpart_head
#         elif n.data % 2 == 0:
#             subpart_tail = n
#         elif subpart_head is not None and subpart_tail.next.data % 2 == 1:
#             rest_nodes = subpart_tail.next
#             new_head = rest_nodes
#             temp = subpart_head
#             while temp != rest_nodes:
#                 next_node = temp.next
#                 temp.next = new_head
#                 new_head = temp
#                 temp = next_node
#             subpart_overhead.next = new_head
#         n = n.next
#     return head


# def subpart_even_reverse(head):
#     """
#     2 cases -
#     1. A subpart starts from the head
#     2. A subpart starts somewhere middle
#     For case 1 - If head is even then we start from and reverse the subpart in place
#     For case 2 - If we find an even number in the middle then we start the reverse
#     :param head: A singly linked list
#     :return: The subparts reversed
#     """
#     if head.data % 2 == 0 and head.next.data % 2 == 0:
#         head, rest_nodes_start = reverse_subpart(head)
#         n = rest_nodes_start
#     else:
#         n = head.next
#     # if we enter the first if condition we start after the first subpart
#     # else we start from the second node as it is how the conditional block was set up
#     while n is not None:
#         # We check for subparts from n.next
#         # if subpart found and reversed n.next = subhead
#         if n.next.data % 2 == 0 and n.next.next.data % 2 == 0:
#             sub_head, rest_nodes_start = reverse_subpart(n.next)
#             n.next = sub_head
#             # as we have iterated and reversed the whole sub part we start from where the sub_part ends
#             n = rest_nodes_start
#             # if finished we break
#             if n is None:
#                 break
#             # if the next node or n.next.next node is None no point in staying in loop and checking
#             if n.next is None or n.next.next is None:
#                 break
#         else:
#             n = n.next
#     return head


def subpart_even_reverse(head):
    """
    Reverse all subparts of the linked list that contain only even integers.

    There are two cases:
    1. A subpart starts from the head.
    2. A subpart starts somewhere in the middle.

    For case 1: If the head node is even, we start from it and reverse the subpart in place.
    For case 2: If we find an even number in the middle, we start the reverse from there.

    :param head: The head of the singly linked list.
    :return: The head of the linked list with reversed subparts.
    """
    # Check if the first two elements are even
    if head.data % 2 == 0 and head.next.data % 2 == 0:
        head, rest_nodes_start = reverse_subpart(head)
        current_node = rest_nodes_start
    else:
        current_node = head.next
    # Iterate through the list to find and reverse subparts
    while current_node is not None:
        # If a subpart is found, reverse it
        if current_node.next is not None and current_node.next.data % 2 == 0:
            sub_head, rest_nodes_start = reverse_subpart(current_node.next)
            current_node.next = sub_head
            current_node = rest_nodes_start
            # Check if reached end of list
            if current_node is None or current_node.next is None:
                break
        else:
            current_node = current_node.next
    return head



# def reverse_subpart(sub_head):
#     """
#     We iterate to the sub tail so that we can get the node which until we have to reverse
#     :param sub_head: From where the subparts even starts
#     :return: the reversed subparts newhead and the the point where the subparts ends and odd node or None starts
#     """
#     sub_tail = sub_head
#     while sub_tail.next is not None:
#         if sub_tail.next.data % 2 == 0:
#             sub_tail = sub_tail.next
#         else:
#             break
#     rest_of_the_nodes = sub_tail.next
#     new_head = rest_of_the_nodes
#     while sub_head is not rest_of_the_nodes:
#         next_node = sub_head.next
#         sub_head.next = new_head
#         new_head = sub_head
#         sub_head = next_node
#     return new_head, rest_of_the_nodes


def reverse_subpart(sub_head):
    """
    Reverse a subpart of the linked list starting from sub_head.

    We iterate to the subtail to determine the end of the subpart that needs to be reversed.

    :param sub_head: The starting node of the even-numbered subpart.
    :return: The new head of the reversed subpart and the node where the subpart ends and the odd node or None starts.
    """
    sub_tail = sub_head
    # Find the end of the subpart
    while sub_tail.next is not None:
        if sub_tail.next.data % 2 == 0:
            sub_tail = sub_tail.next
        else:
            break
    # Save the rest of the nodes after the subpart
    rest_of_the_nodes = sub_tail.next
    new_head = rest_of_the_nodes
    # Reverse the subpart
    while sub_head is not rest_of_the_nodes:
        next_node = sub_head.next
        sub_head.next = new_head
        new_head = sub_head
        sub_head = next_node
    return new_head, rest_of_the_nodes



list1 = [2, 18, 24, 3, 5, 7, 9, 6, 12]
head1 = create_list(list1)
iterate_list(head1)
print("========")
head1 = (subpart_even_reverse(head1))
iterate_list(head1)

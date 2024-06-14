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


def remove_even_node(head):
    """
    1. Traverse the linked list
    2. If we find an even node make appropriate connection changes
    :param head: The head starts with an odd number
    :return: The removed even node
    """
    n = head
    while n is not None:
        if n.next.data % 2 == 0:
            removed_node = n.next
            n.next = removed_node.next
            removed_node.next = None
            return removed_node
        n = n.next


def even_first(head):
    """
    Insertion point is where after the firs part of even ends so the last node of the first even sub part is insertion
    point
    1. First we find the insertion point if the linked list starts with even
    2. If the linked list starts with odd we get the first even and make it head and make it insertion point
    3. We traverse from insertion_point.next to the last node of the given linked list
    4. If the current nodes next node is even we remove it and insert it with the help of remove_even_node()
    5. When inserting we do not traverse as one node otherwise gets skipped, so we continue
    :param head:
    :return:
    """
    if head.data % 2 == 0:
        n = head
        while n is not None:
            if n.next.data % 2 == 1:
                break
            n = n.next
        insertion_point = n

    else:
        node_to_insert = remove_even_node(head)
        node_to_insert.next = head
        head = node_to_insert
        insertion_point = head
    current_node = insertion_point.next

    while current_node.next is not None:
        if current_node.next.data % 2 == 0:
            node_to_insert = remove_even_node(current_node)
            node_to_insert.next = insertion_point.next
            insertion_point.next = node_to_insert
            insertion_point = insertion_point.next
            continue
        current_node = current_node.next
    return head



# def even_first(head):
#     """
#     1. We make the first even number head
#     2. Remove its previous links
#     3. The rest of the even goes to a pointer that first points the insertion after head, then after the first two node
#         and so on
#     4. Repeat step 2
#     :param head:
#     :return:
#     """
#     if head.data % 2 == 0:
#         head_is_even = True
#         insertion_point = head
#     else:
#         head_is_even = False
#
#     current_node = head
#     while current_node is not None:
#         if not head_is_even:
#             if current_node.next.data % 2 == 0:
#                 removed_node = current_node.next
#
#                 current_node.next = removed_node.next
#                 removed_node.next = head
#
#                 # changing head
#                 head = removed_node
#
#                 insertion_point = removed_node
#                 head_is_even = True
#         else:
#             if current_node.next.data % 2 == 0 and current_node.data % 2 == 1:
#                 removed_node = current_node.next
#
#                 current_node.next = removed_node.next
#                 removed_node.next = insertion_point.next
#                 insertion_point.next = removed_node
#
#                 insertion_point = removed_node
#         current_node = current_node.next
#     return head


list1 = [17, 15, 8, 12, 10, 5, 4, 1, 7, 6]
head1 = create_list(list1)
head1 = even_first(head1)
iterate_list(head1)

list2 = [8, 12, 10, 5, 4, 1, 6]
head2 = create_list(list2)
head2 = even_first(head2)
iterate_list(head2)
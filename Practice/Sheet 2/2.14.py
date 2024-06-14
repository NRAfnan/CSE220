class Node:
    def __init__(self, data, nxt, prev):
        self.data = data
        self.next = nxt
        self.prev = prev


def create_list(lst):
    n = Node(lst[0], None, None)
    head = n
    tail = head
    i = 1
    while i < len(lst):
        n = Node(lst[i], None, tail)
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


def r_iterate_list(head):
    n = head
    while n.next is not None:
        n = n.next

    while n is not None:
        print(n.data)
        n = n.prev


# def reverse_in_place(head):
#     n = head
#     new_head = None
#     while n is not None:
#         nxt = n.next
#         n.next = new_head
#         new_head = n
#         n = nxt
#
#     n = new_head
#     tail = None
#     while n is not None:
#         nxt = n.prev
#         n.prev = tail
#         tail = n
#         n = nxt
#     return new_head


def reverse_in_place(head):
    current = head
    while current is not None:
        # Swap next and prev pointers
        current.next, current.prev = current.prev, current.next
        # Move to the next node
        current = current.prev  # Move to the previous node as next and prev are swapped

    # Find the new head, as head is the tail now
    while head.prev is not None:
        head = head.prev

    return head


head1 = create_list([10, 20, 30, 40, 50])
iterate_list(head1)
head1 = reverse_in_place(head1)
iterate_list(head1)
print("Reverse")
r_iterate_list(head1)
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
        print(n.data)
        n = n.next


def find_intersection(head1, head2):
    n1 = head1
    n2 = head2
    intersect_head = None
    tail = intersect_head
    while n1 is not None:
        while n2 is not None:
            if intersect_head is None and n1.data == n2.data:
                n = Node(n1.data, None)
                intersect_head = n
                tail = intersect_head
            elif n1.data == n2.data:
                n = Node(n1.data, None)
                tail.next = n
                tail = tail.next
            n2 = n2.next
        n2 = head2
        n1 = n1.next
    return intersect_head


head1 = create_list([1, 2, 3, 4, 5])
head2 = create_list([2, 3, 4])
head3 = find_intersection(head1, head2)
iterate_list(head3)
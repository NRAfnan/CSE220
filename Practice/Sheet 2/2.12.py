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


def node_at(head, idx):
    n = head
    i = 0
    while n is not None:
        if i == idx:
            return n
        i += 1
        n = n.next
    return None


def count_ns(head):
    n = head
    count = 0
    while n is not None:
        count += 1
        n = n.next
    return count


def swap(head, k):
    len_head = count_ns(head)
    if len_head % 2 == 0 and k == len_head // 2:
        n1_prev = node_at(head, k - 1 - 1)
        n1 = n1_prev.next

        n2_prev = node_at(head, len_head - k - 1)
        n2 = n2_prev.next

        n1.next = n2.next
        n1_prev.next = n2
        n2.next = n1

    else:
        n1_prev = node_at(head, k - 1 - 1)
        n1 = n1_prev.next
        n1_next = n1.next

        n2_prev = node_at(head, len_head - k - 1)
        n2 = n2_prev.next
        n2_next = n2.next

        n1_prev.next = n2
        n2.next = n1_next

        n2_prev.next = n1
        n1.next = n2_next

    return head


head1 = create_list([1, 2, 3, 4, 5])
iterate_list(head1)
swap(head1, 2)
iterate_list(head1)
# print('++')
# print(head1.data)
# print(head1.next.data)
# print(head1.next.next.data)
# print(head1.next.next.next.data)
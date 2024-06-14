class Node:
    def __init__(self, data, nxt, prev):
        self.data = data
        self.next = nxt
        self.prev = prev


def create_list(given_list):
    dh = Node("Dummy head", None, None)
    dh.next = dh
    dh.prev = dh
    tail = dh
    i = 0
    while i < len(given_list):
        n = Node(given_list[i], dh, tail)
        tail.next = n
        tail = tail.next
        dh.prev = tail
        i += 1
    return dh


def iterate_list(dh):
    n = dh.next
    while n != dh:
        print(n.data)
        n = n.next


def right_rotate_k_times(dh, k):
    for i in range(0, k):
        right_rotate(dh)
    return dh


def right_rotate(dh):
    node_to_rotate = dh.prev
    second_last_node = node_to_rotate.prev
    first_node = dh.next

    dh.next = node_to_rotate
    node_to_rotate.prev = dh

    node_to_rotate.next = first_node
    first_node.prev = node_to_rotate

    second_last_node.next = dh
    dh.prev = second_last_node

    return dh


def r_iterate_list(dh):
    n = dh.prev

    while n != dh:
        print(n.data)
        n = n.prev


head1 = create_list([10, 20, 30, 40])
right_rotate_k_times(head1, 2)
iterate_list(head1)
print("======")
r_iterate_list(head1)
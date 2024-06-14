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


def left_rotate_k_times(dh, k):
    for i in range(0, k):
        left_rotate(dh)
    return dh


def left_rotate(dh):
    node_to_rotate = dh.next
    last_node = dh.prev

    dh.next = node_to_rotate.next
    node_to_rotate.next.prev = dh

    last_node.next = node_to_rotate
    node_to_rotate.prev = last_node

    dh.prev = node_to_rotate
    node_to_rotate.next = dh

    return dh


def r_iterate_list(dh):
    n = dh.prev

    while n != dh:
        print(n.data)
        n = n.prev


head1 = create_list([10, 20, 30, 40])
left_rotate_k_times(head1, 4)
iterate_list(head1)
print("======")
r_iterate_list(head1)
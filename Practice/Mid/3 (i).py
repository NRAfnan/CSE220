class Node:
    def __init__(self, data, nxt, prev):
        self.data = data
        self.next = nxt
        self.prev = prev


def create_list(lst):
    dh = Node("Dummy head", None, None)
    dh.next = dh
    dh.prev = dh
    tail = dh

    i = 0
    while i < len(lst):
        n = Node(lst[i], dh, tail)
        tail.next = n
        tail = tail.next
        dh.prev = tail
        i += 1
    return dh


def iterate_list(head):
    n = head.next
    while n is not head:
        if n.next is not head:
            print(n.data, end=" ")
        else:
            print(n.data)
        n = n.next


dh1 = create_list([10, 20, 30, 40])
#iterate_list(dh1)


def gg(dh):
    for i in range(5):
        for j in range(i):
            n1 = dh.next
            n2 = n1.next
            n3 = dh.prev
            dh.next = n2
            n2.prev = dh
            n3.next = n1
            n1.next = dh
            n1.prev = n3
            dh.prev = n1
        iterate_list(dh1)


gg(dh1)
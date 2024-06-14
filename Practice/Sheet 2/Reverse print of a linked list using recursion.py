class Node:
    def __init__(self, elem, nxt):
        self.elem = elem
        self.next = nxt


def create_list(arr):
    head = Node(arr[0], None)
    tail = head
    i = 1
    while i < len(arr):
        node = Node(arr[i], None)
        tail.next = node
        tail = tail.next
        i += 1
    return head


def iterate_list(head):
    n = head
    while n is not None:
        print(n.elem)
        n = n.next


def reverse_recur(head):
    if head is None:
        return
    reverse_recur(head.next)
    print(head.elem)


list1 = [10, 20, 30, 40, 50]
head1 = create_list(list1)
iterate_list(head1)
print("=======")
reverse_recur(head1)
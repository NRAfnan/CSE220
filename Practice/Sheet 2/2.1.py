class Node:
    def __init__(self, data, nxt):
        self.data = data
        self.next = nxt


def create_list(lst):
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


def move_last_to_first(head):
    n = head
    while n.next.next is not None:
        n = n.next
    second_last = n
    last = second_last.next
    second_last.next = None
    last.next = head
    return last



list1 = [1, 2, 3, 4, 5]
head1 = create_list(list1)
print(type(head1))
iterate_list(head1)
head1 = move_last_to_first(head1)
print("======")
iterate_list(head1)


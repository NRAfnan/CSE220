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


def count_len(head):
    count = 0
    n = head
    while n is not None:
        count += 1
        n = n.next
    print(count)
    return count


def find_nth(head, n):
    lenght_ll = count_len(head)
    idx = lenght_ll - n
    i = 0
    n = head
    while n is not None:
        if idx == i:
            return n.data
        i += 1
        n = n.next


list1 = [10, 20, 30, 40, 50]
head1 = create_list(list1)
print(find_nth(head1, 2))

list1 = [35, 15, 4,  20, 45]
head1 = create_list(list1)
print(find_nth(head1, 4))
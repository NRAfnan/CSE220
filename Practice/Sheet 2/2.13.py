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


def check_palindrome(head):
    is_palindrome = True
    tail = head
    while tail.next is not None:
        tail = tail.next
    n = head
    while n is not None:
        if n.data != tail.data:
            is_palindrome = False
            return is_palindrome
        n = n.next
        tail = tail.prev
    return is_palindrome


head1 = create_list([1, 7, 4, 7, 2])
iterate_list(head1)
print(check_palindrome(head1))
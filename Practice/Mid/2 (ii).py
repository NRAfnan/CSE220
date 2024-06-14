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


def pairwiseEqual(h1, h2):
    is_pairwise = True
    first_prev = h1
    first_curr = h1.next
    second_prev = h2
    second_curr = h2.next
    while first_curr.next is not None:
        print(first_prev.data)
        print(first_curr.data)
        print(second_prev.data)
        print(second_curr.data)

        if first_prev.data == second_prev.data and first_curr.data == second_curr.data:
            is_pairwise = True
        elif first_prev.data == second_curr.data and first_curr.data == second_prev.data:
            is_pairwise = True
        else:
            is_pairwise = False
            break
        first_prev = first_prev.next.next
        first_curr = first_curr.next.next

        second_prev = second_prev.next.next
        second_curr = second_curr.next.next

    print("====")
    print(first_prev.data)
    print(first_curr.data)
    print(second_prev.data)
    print(second_curr.data)
    if first_prev.data == second_prev.data and first_curr.data == second_curr.data:
        is_pairwise = True
    elif first_prev.data == second_curr.data and first_curr.data == second_prev.data:
        is_pairwise = True
    else:
        is_pairwise = False
    return is_pairwise


head1 = create_list([10, 15, 34, 41])
head2 = create_list([15, 10, 34, 41])
print(pairwiseEqual(head2, head1))
head3 = create_list([10, 15, 34, 42])
head4 = create_list([15, 10, 34, 41])
print(pairwiseEqual(head3, head4))
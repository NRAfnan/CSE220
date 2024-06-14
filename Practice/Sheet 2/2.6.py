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


def find_middle(head):
    """
        Using the hare and tortoise algo
        1. Initialize slow = head
        2. Initialize head = slow
        3. While fast is not the last node or none itself
        4. Let slow traverse 1 step at a time and fast 2 step at a time
        """
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    print(slow.data)


list1 = [10, 20, 30, 40, 50]
head1 = create_list(list1)
find_middle(head1)

list2 = [1, 2, 3, 4, 5, 6]
head2 = create_list(list2)
find_middle(head2)
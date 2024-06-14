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
    return count


def node_at(head, idx):
    i = 0
    n = head
    while n is not None:
        if i == idx:
            return n
        i += 1
        n = n.next
    return None


# def check_palindrome(head):
#     is_palindrome = True
#     i = 0
#     print(count_len(head))
#     while i < count_len(head):
#         n1 = node_at(head, i)
#         n2 = node_at(head, count_len(head) - 1 - i)
#         if n1.data != n2.data:
#             is_palindrome = False
#             return is_palindrome
#         i += 1
#     return is_palindrome


def reverse_list(head):
    # in place
    new_head = None
    n = head
    while n is not None:
        nxt = n.next
        n.next = new_head
        new_head = n
        n = nxt
    return new_head


def middle_node(head):
    """
    Using the hare and tortoise algo
    1. Initialize slow = head
    2. Initialize head = slow
    3. While fast.next is not None and fast.next.next is not None
    4. Let slow traverse 1 step at a time and fast 2 step at a time
    :param head: Head of given the linked list
    :return: return the middle node for odd number of nodes and first middle node for even number of nodes
    """
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def check_palindrome(head):
    if head is None or head.next is None:
        return True

    # Find the middle of the linked list for odd number of nodes and first middle node for even number of nodes
    mid = middle_node(head)

    # Reverse the second half of the linked list
    second_half = reverse_list(mid.next)

    # Compare the first half with the reversed second half
    first_half = head
    while second_half is not None:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


list1 = [1, 2, 3, 1, 1]
head1 = create_list(list1)
print(check_palindrome(head1))
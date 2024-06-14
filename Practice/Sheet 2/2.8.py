class Node:
    def __init__(self, data, nxt):
        self.data = data
        self.next = nxt


def create_class(given_list):
    head = Node(given_list[0], None)
    tail = head
    i = 1
    while i < len(given_list):
        n = Node(given_list[i], None)
        tail.next = n
        tail = tail.next
        i += 1
    return head


def iterate_list(head):
    n = head
    while n is not None:
        print(n.data)
        n = n.next


def algorithm_delete(num_friends, friends_need_to_del, head):
    """
    1. For head keep removing head until number of friends that we need to delete is deleted
        or head.data > head.next.data
    2. The next nodes data should be less than the next nodes and its next nodes data
    3. And for that wee need to check the current_node.next is not None and Current_node.next.next
        is not None only then can we compare
    4. Lastly again check for head and delete if friends need to delete is no zero
    :param num_friends: Number of friends which we dont have any work with
    :param friends_need_to_del: Number of friends we need to delete
    :param head: Linked list head
    :return: Deleted friend lists linked list head
    """
    head, friends_need_to_del = delete_head(head, friends_need_to_del)

    # compare next two nodes and delete
    current_node = head
    while current_node.next is not None and current_node.next.next:
        if friends_need_to_del == 0:
            break
        if current_node.next.data < current_node.next.next.data:
            current_node.next = current_node.next.next
            friends_need_to_del -= 1
            # we continue when we delete one element cuz otherwise the next node that has been shifted will get skipped
            continue
        current_node = current_node.next

    head, friends_need_to_del = delete_head(head, friends_need_to_del)
    return head


def delete_head(head, need_to_delete):
    head_skipped = 0
    while head_skipped < need_to_delete:
        if head.data < head.next.data:
            head = head.next
        else:
            break
        head_skipped += 1
    need_to_delete -= head_skipped
    return head, need_to_delete


head1 = create_class([23, 45, 11, 77, 18])
head1 = algorithm_delete(5, 3, head1)
iterate_list(head1)
print("======")
head1 = create_class([19, 12, 3, 4, 17])
head1 = algorithm_delete(5, 2, head1)
iterate_list(head1)
print("======")
head1 = create_class([3, 100, 1])
head1 = algorithm_delete(3, 1, head1)
iterate_list(head1)
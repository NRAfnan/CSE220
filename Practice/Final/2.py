class Node:
    def __init__(self, elem, nxt=None):
        self.elem = elem
        self.next = nxt


def sum_dist(LL1, dist):
    result = 0
    for i in dist:
        is_found = False
        j = 0
        temp = LL1
        while temp is not None:
            if j == i:
                is_found = True
                break
            j += 1
            temp = temp.next
        if is_found:
            result += temp.elem
        else:
            result += 0
    return result


head = Node(10)
head.next = Node(16)
head.next.next = Node(-5)
head.next.next.next = Node(9)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(4)
dist = [2, 0, 5, 2, 8]
print(sum_dist(head, dist))
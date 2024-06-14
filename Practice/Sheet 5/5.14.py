class Node:
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None


def print_at_k_distance(root, k):
    if root is None:
        return
    if k == 0:
        print(root.elem, end=" ")
        return
    print_at_k_distance(root.left, k - 1)
    print_at_k_distance(root.right, k - 1)


root1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node8 = Node(8)

root1.left = node2
root1.right = node3

node2.left = node4
node2.right = node5

node3.left = node8

print_at_k_distance(root1, 2)
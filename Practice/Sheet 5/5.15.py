class Node:
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None


def print_ancestors(root, key):
    if root is None:
        return False
    if root.elem == key:
        return True
    if print_ancestors(root.left, key) or print_ancestors(root.right, key):
        print(root.elem)
        return True
    return False


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

node4.left = node8

print_ancestors(root1, 7)
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None


root = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)


root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node3.left = node5
node3.right = node6

node2.left = node7
node2.right = node8


def pre_print(root):
    if root is None:
        return
    pre_print(root.left)
    pre_print(root.right)
    print(root.elem)


def get_height(n):
    if n is None:
        return - 1
    return 1 + max(get_height(n.left), get_height(n.right))


print(get_height(root))

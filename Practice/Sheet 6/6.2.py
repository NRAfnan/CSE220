class Node:
    def __init__(self, elem):
        self.elem = elem
        self.left = self.right = None


def insert_node(root, k):
    if root is None:
        root = Node(k)
    if root.elem == elem:
        return root
    if k < root.elem:
        root.left = insert_node(root.left, k)
    if k > root.elem:
        root.right = insert_node(root.right, k)
    return root
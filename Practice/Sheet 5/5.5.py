# mile nai
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None


def tree_constructor(g_list, i, length):
    root = None
    if i < length:
        if g_list[i] is not None:
            root = Node(g_list[i])
            root.left = tree_constructor(g_list, 2 * i, length)
            root.right = tree_constructor(g_list, (2 * i) + 1, length)
    return root


tuple1 = [None, 15, 25, 35, 10, 35, 15, 18, None, None, None, 33,  None, 5, None, 19, None, None, None, 16]
tree_constructor(tuple1, 1, len(tuple1))

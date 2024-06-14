class Node:
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None


def checkSum(root):
    if root.left is None and root.right is None:
        return True
    if root.left is None:
        if root.elem == root.right.elem:
            return checkSum(root.right)
        else:
            return False
    elif root.right is None:
        if root.elem == root.left.elem:
            return checkSum(root.left)
        else:
            return False
    else:
        if root.elem == (root.left.elem + root.right.elem):
            return checkSum(root.left) and checkSum(root.right)
        else:
            return False


root = Node(10)
node1 = Node(6)
node2 = Node(4)

node3 = Node(3)
node4 = Node(1)

root.left = node1
root.right = node2

node2.left = node3
node2.right = node4

print(checkSum(root))
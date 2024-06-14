class Node:
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None


def isMirror(r1, r2):
    if r1 is None and r2 is None:
        return True
    if r1 is None or r2 is None:
        return False
    if r1.elem == r2.elem:
        return isMirror(r1.left, r2.right) and isMirror(r1.right, r2.left)
    return False


def isSymmetric(root):
    if root is None:
        return False
    return isMirror(root.left, root.right)


root1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node5 = Node(2)
node6 = Node(4)
node7 = Node(3)

root1.left = node2
root1.right = node5

node2.left = node3
node2.right = node4

node5.left = node6
node5.right = node7

print(isSymmetric(root1))


print("===Case2===")

root1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node5 = Node(2)
node6 = Node(4)
node7 = Node(3)

root1.left = node2
root1.right = node5
#
# node2.left = node3
node2.right = node3
#
# node5.left = node6
node5.right = node7

print(isSymmetric(root1))
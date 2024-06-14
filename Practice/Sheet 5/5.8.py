class newNode:
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None


def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    elif root1.elem == root2.elem and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right):
        return True
    else:
        return False


root1 = newNode(5)
root2 = newNode(5)

root1.left = newNode(3)
root1.right = newNode(8)
root1.left.left = newNode(2)
root1.left.right = newNode(4)

root2.left = newNode(3)
root2.right = newNode(8)
root2.left.left = newNode(2)
root2.left.right = newNode(4)

if isIdentical(root1, root2):
    print("Both BSTs are identical")
else:
    print("BSTs are not identical")
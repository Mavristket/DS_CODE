class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def isSameTree(a, b):

    if a is None and b is None:
        return True

    if a is None or b is None:
        return False

    if a.val != b.val:
        return False

    return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)


def isSubtree(root, subRoot):

    if root is None:
        return False

    if isSameTree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isMirror(t1, t2):
    if t1 is None and t2 is None:
        return True

    if t1 is None or t2 is None:
        return False

    return (t1.val == t2.val and
            isMirror(t1.left, t2.right) and
            isMirror(t1.right, t2.left))


def isSymmetric(root):
    if root is None:
        return True

    return isMirror(root.left, root.right)

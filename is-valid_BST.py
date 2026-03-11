class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def validateBST(root, min_val=float('-inf'), max_val=float('inf')):

    if root is None:
        return True

    if root.val <= min_val or root.val >= max_val:
        return False

    return (validateBST(root.left, min_val, root.val) and
            validateBST(root.right, root.val, max_val))
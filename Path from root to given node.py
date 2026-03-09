class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def find_path(root, target, path):

    if root is None:
        return False

    # add current node
    path.append(root.val)

    # if target found
    if root.val == target:
        return True

    # search left or right
    if find_path(root.left, target, path) or find_path(root.right, target, path):
        return True

    # remove node if not in path
    path.pop()
    return False
    
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_lca(root, p, q):

    if root is None:
        return None

    if root.value == p or root.value == q:
        return root

    left = find_lca(root.left, p, q)
    right = find_lca(root.right, p, q)

    if left and right:
        return root

    if left:
        return left

    return right
def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True

    if not (min_val < root.value < max_val):
        return False

    return (is_bst(root.left, min_val, root.value) and
            is_bst(root.right, root.value, max_val))
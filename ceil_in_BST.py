def ceil(root):
    ceil=-1
    while root:
        if root.value==x:
            return root.value
        if root.value<x:
            root=root.right
        else:
            ceil=root.value
            root=root.left
    return ceil
def flooe(root):
    floor=-1
    while root:
        if root.value==x:
            return root.value
        if root.value>x:
            root=root.left
        else:
            floor=root.value
            root=root.right
    return floor


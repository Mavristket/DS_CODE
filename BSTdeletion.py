# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Insert function (for building tree)
def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


# Find minimum value node (used in delete)
def findMin(root):
    while root.left:
        root = root.left
    return root


# Delete function
def delete(root, value):
    if root is None:
        return root

    # Step 1: Find the node
    if value < root.value:
        root.left = delete(root.left, value)

    elif value > root.value:
        root.right = delete(root.right, value)

    else:
        # Node found 🔥

        # Case 1: No child
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        elif root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        # Case 3: Two children
        temp = findMin(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)

    return root


# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


# Main
root = None
elements = [50, 30, 70, 20, 40, 60, 80]

for ele in elements:
    root = insert(root, ele)

print("Before Deletion:")
inorder(root)

root = delete(root, 30)

print("\nAfter Deleting 30:")
inorder(root)




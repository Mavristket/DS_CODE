# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Insert function (to build BST)
def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


# Search function
def search(root, key):
    # If tree is empty
    if root is None:
        return False

    # If element found
    if root.value == key:
        return True

    # If key is smaller → search left
    elif key < root.value:
        return search(root.left, key)

    # If key is greater → search right
    else:
        return search(root.right, key)


# Main
root = None
elements = [50, 30, 70, 20, 40, 60, 80]

for ele in elements:
    root = insert(root, ele)

key = 60

if search(root, key):
    print("Element Found")
else:
    print("Element Not Found")
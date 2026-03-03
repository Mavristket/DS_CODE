# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Height function
def height(root):
    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    return 1 + max(left_height, right_height)


# Example Tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

print("Height of tree:", height(root))
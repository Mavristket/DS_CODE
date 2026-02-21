class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    # Get height
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factor
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    # Right Rotate (LL Case)
    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    # Left Rotate (RR Case)
    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    # Insert function
    def insert(self, root, value):

        # Step 1: Normal BST insert
        if not root:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        # Step 2: Update height
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Step 3: Get balance
        balance = self.getBalance(root)

        # Step 4: Check 4 cases

        # LL Case
        if balance > 1 and value < root.left.value:
            return self.rightRotate(root)

        # RR Case
        if balance < -1 and value > root.right.value:
            return self.leftRotate(root)

        # LR Case
        if balance > 1 and value > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # RL Case
        if balance < -1 and value < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Preorder traversal
    def preorder(self, root):
        if not root:
            return
        print(root.value, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)


# ---------------- MAIN ----------------

tree = AVLTree()
root = None

nums = [10, 20, 30, 40, 50, 25]

for num in nums:
    root = tree.insert(root, num)

print("Preorder traversal of AVL tree:")
tree.preorder(root)
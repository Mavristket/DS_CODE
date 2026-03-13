class Solution:
    def kthSmallest(self, root, k):
        arr = []

        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)

        return arr[k-1]
class Solution:
    def kthLargest(self, root, k):
        self.k = k
        self.result = None

        def reverse_inorder(node):
            if not node or self.result is not None:
                return

            reverse_inorder(node.right)

            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return

            reverse_inorder(node.left)

        reverse_inorder(root)
        return self.result
        
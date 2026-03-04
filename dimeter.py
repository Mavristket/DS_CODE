class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            # update diameter
            self.diameter = max(self.diameter, left_height + right_height)
            
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter
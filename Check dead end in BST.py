def deadEnd(root):
    
    def solve(node, min_val, max_val):
        
        if node is None:
            return False
        
        # dead end condition
        if min_val == max_val:
            return True
        
        return (solve(node.left, min_val, node.val - 1) or
                solve(node.right, node.val + 1, max_val))
    
    return solve(root, 1, float('inf'))

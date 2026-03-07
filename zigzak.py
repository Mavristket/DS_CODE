class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def zigzag(root):
    if root is None:
        return []
    q=deque([root])
    result=[]
    left_to_right=True
    while q:
        n=len(q)
        level=[]
        for i in range(n):
            node=q.popleft()
            level.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if not left_to_right:
            level.reverse()
        result.append(level)
        left_to_right=not left_to_right
    return result


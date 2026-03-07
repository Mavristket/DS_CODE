class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
def right_view(root):
    if root is None:
        return []
    q=deque([root])
    result=[]
    while q:
        n=len(q)
        for i in range(n):
            node=q.popleft()
            if i==n-1:
                result.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.qppend(node.right)
    return result

            
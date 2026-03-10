class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def levelsum(root):
    if root is None:
        return []
    q=deque([root])
    while q:
        size=len(q)
        level_sum=0

        for i in range(size):
            node=q.popleft()
            level_sum+=node.value
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print(level_sum)

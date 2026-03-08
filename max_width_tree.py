from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def maxWidth(root):

    if root is None:
        return 0

    q = deque([(root,0)])
    max_width = 0

    while q:

        size = len(q)
        first = q[0][1]
        last = q[-1][1]

        width = last - first + 1
        max_width = max(max_width,width)

        for i in range(size):

            node,index = q.popleft()

            if node.left:
                q.append((node.left,2*index))

            if node.right:
                q.append((node.right,2*index+1))

    return max_width
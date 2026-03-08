from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def countNodesAtLevelK(root, k):

    if root is None:
        return 0

    q = deque([root])
    level = 0

    while q:

        size = len(q)

        if level == k:
            return size

        for i in range(size):

            node = q.popleft()

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        level += 1

    return 0
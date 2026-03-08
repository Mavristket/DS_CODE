from collections import defaultdict, deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def verticalTraversal(root):

    if root is None:
        return []

    column_table = defaultdict(list)
    q = deque([(root,0)])

    while q:

        node,col = q.popleft()

        column_table[col].append(node.val)

        if node.left:
            q.append((node.left,col-1))

        if node.right:
            q.append((node.right,col+1))

    result = []

    for col in sorted(column_table.keys()):
        result.append(column_table[col])

    return result
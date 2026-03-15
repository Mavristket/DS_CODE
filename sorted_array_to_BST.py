class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sortedArrayToBST(arr, start, end):

    if start > end:
        return None

    mid = (start + end) // 2

    root = Node(arr[mid])

    root.left = sortedArrayToBST(arr, start, mid-1)
    root.right = sortedArrayToBST(arr, mid+1, end)

    return root


arr = [1,2,3,4,5,6,7]

root = sortedArrayToBST(arr, 0, len(arr)-1)

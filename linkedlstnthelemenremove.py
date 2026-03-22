class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def removeNthFromEnd(head, n):
    # Step 1: count total nodes
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next

    # Step 2: find position to delete
    pos = count - n

    # Step 3: if head needs to be removed
    if pos == 0:
        return head.next

    # Step 4: go to node before target
    temp = head
    for _ in range(pos - 1):
        temp = temp.next

    # Step 5: delete node
    temp.next = temp.next.next

    return head
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.value


# Create Linked List: 1→2→3→4→5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Middle:", find_middle(head))
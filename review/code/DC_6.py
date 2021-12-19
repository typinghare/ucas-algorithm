class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(lists):
    length = len(lists)

    # conquer
    if length == 0:
        return None
    if length == 1:
        # return the only list
        return lists[0]

    # divide
    mid = length >> 1
    list1 = solve(lists[:mid])
    list2 = solve(lists[mid:])

    # combine - merge list1 and list2
    node1, node2 = list1, list2
    head = ListNode()
    node = head
    while node1 is not None and node2 is not None:
        if node1.val < node2.val:
            node.next = node1
            node1 = node1.next
        else:
            node.next = node2
            node2 = node2.next
        node = node.next

    while node1 is not None:
        node.next = node1
        node1 = node1.next
        node = node.next

    while node2 is not None:
        node.next = node2
        node2 = node2.next
        node = node.next

    return head.next


s = [
    ListNode(1, ListNode(2, ListNode(2))),
    ListNode(1, ListNode(1, ListNode(2))),
]

r = solve(s)
while r is not None:
    print(r.val)
    r = r.next

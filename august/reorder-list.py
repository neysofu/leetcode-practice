# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def length(head):
    current = head
    length = 0
    while current is not None:
        length += 1
        current = current.next
    return length

def nth(head, i):
    current = head
    for _ in range(i):
        current = current.next
    return current

def reverse(head):
    previous = None
    next = head.next
    while head is not None:
        tmp = head.next
        head.next = previous
        previous = head
        head = tmp
    return previous

def interweaveTwoHalves(lane1, lane2):
    while lane2 is not None:
        tmp = lane2.next
        lane2.next = lane1.next
        lane1.next = lane2
        lane1 = lane2.next
        lane2 = tmp

class Solution:
    def reorderList(self, head) -> None:
        if head is None or head.next is None:
            return
        """
        Do not return anything, modify head in-place instead.
        """
        # Note that `pivot` will be the last element of `lane1`.
        pivot = nth(head, (length(head) - 1) // 2)
        secondHalf = pivot.next
        secondHalf = reverse(pivot.next)
        pivot.next = None
        interweaveTwoHalves(head, secondHalf)

Solution.reorderList(None, ListNode(0, ListNode(1, None)))
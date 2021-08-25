class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        tail = head
        lists = [l for l in lists if l is not None]
        while len(lists) > 0:
            best = lists[0].val
            best_i = -1
            for i in range(len(lists)):
                if best is None or lists[i].val <= best:
                    best = lists[i].val
                    best_i = i
            tail.next = lists[best_i]
            tail = tail.next
            lists[best_i] = tail.next
            lists = [l for l in lists if l is not None]
        return head.next
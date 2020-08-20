from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def optional_iter(node: Optional[ListNode]):
        if node is None:
            return (0, None)
        else:
            return (node.val, node.next)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        node = ListNode(0, None)
        initial_node = node
        while l1 or l2 or carry:
            digit1, l1 = ListNode.optional_iter(l1)
            digit2, l2 = ListNode.optional_iter(l2)
            result = digit1 + digit2 + carry
            carry = result // 10
            result %= 10
            node.next = ListNode(result, None)
            node = node.next
        return initial_node.next
    
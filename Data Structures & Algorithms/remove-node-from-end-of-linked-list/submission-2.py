# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        left, right = head, head

        for _ in range(n):
            if not right.next:
                return left.next
            right = right.next
        
        while right and right.next:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return head
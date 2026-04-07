# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
        
        stack = []
        while slow:
            stack.append(slow)
            slow = slow.next
        
        temp = head
        while stack:
            dummy = temp.next
            temp.next = stack.pop(-1)
            temp.next.next = dummy
            temp = dummy
        
        temp.next = None

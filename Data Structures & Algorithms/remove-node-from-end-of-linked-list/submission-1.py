# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        indToRemove = length - n
        res = ListNode()
        res.next = head
        temp = res
        for _ in range(indToRemove):
            temp = temp.next
        
        temp.next = temp.next.next

        return res.next
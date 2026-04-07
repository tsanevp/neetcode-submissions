# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            l1 = lists.pop(-1)
            l2 = lists.pop(-1)
            lists.append(self.mergeLists(l1, l2))
        
        return lists[0]
    
    def mergeLists(self, l1, l2) -> Optional[ListNode]:
        res = ListNode()
        temp = res

        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            
            temp = temp.next
        
        if l1:
            temp.next = l1
        
        if l2:
            temp.next = l2
        
        return res.next
                
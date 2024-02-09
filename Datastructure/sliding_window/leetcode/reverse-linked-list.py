# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
                return head
            
        dummy = head.next
        res = head
        _next = None
        while dummy:
            res.next = _next
            _next = res
            res = dummy
            dummy = dummy.next
            
        res.next = _next  
        return res
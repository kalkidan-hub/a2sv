# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        _len = 0
        original = head 
        
        while head:
            _len += 1
            head = head.next
        
        res = 0
        while original:
            res += original.val * (2 **( _len - 1))
            _len -= 1
            original = original.next
            
        return res
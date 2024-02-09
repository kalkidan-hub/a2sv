# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # inset in between at kth position
        # not to be used function, tho
        
        def insertNode(ll,k,inL):
            pos = 0
            l = n = ll
            
            while pos < k:
                pos += 1
                prev = n
                n = n.next
            
            prev.next = inL
            inL.next = n
            
            return l
        
        
        dummy = res = ListNode()
        
        while list1 and list2:
            
            if list1.val <= list2.val:
                res.next = ListNode(list1.val)
                list1 = list1.next
            else:
                res.next = ListNode(list2.val)
                list2 = list2.next
            
            res = res.next
        
        if list1:
            res.next = list1
        if list2:
            res.next = list2
       
        
        return dummy.next
        
        
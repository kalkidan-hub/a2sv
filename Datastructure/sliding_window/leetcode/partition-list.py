# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        greaters = ListNode()
        greater_head = greaters
        lessers = ListNode()
        lessers_head = lessers
        while head:
            if head.val < x:
                lessers.next = ListNode(head.val)
                lessers = lessers.next
            else:
                greaters.next = ListNode(head.val)
                greaters = greaters.next
            
            head = head.next
        
        
        lessers.next = greater_head.next
        return lessers_head.next
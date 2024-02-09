# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        slow = head
        fast = head
        
        while True:
            
            
            # slow = slow.next
            
            if fast and fast.next:
                fast = fast.next.next
            
            if not slow or not fast or not fast.next:
                break
                
            if slow == fast:
                return True
            
            slow = slow.next
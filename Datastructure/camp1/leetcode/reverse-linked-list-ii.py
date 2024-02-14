# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev, curr = dummy,head
        for _ in range(left - 1):
            prev, curr = curr, curr.next

        act_prev = None
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = act_prev
            act_prev = curr
            curr = tmp

        prev.next.next = curr
        prev.next = act_prev
       

        return dummy.next
             

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        right, left = head, head
        while right:
            while left and left.val == right.val:
                left = left.next
            right.next = left
            right = left
        return head        
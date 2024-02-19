# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        while head:
            node = ListNode(head.val)
            curr = dummy
            while curr.next and curr.next.val < node.val:
                curr = curr.next
            tmp = curr.next
            curr.next = node
            node.next = tmp

            head = head.next
            
        return dummy.next
            
        
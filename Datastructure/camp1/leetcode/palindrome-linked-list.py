# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # identify the middle element
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        def reverse(head):
            prev, curr = None, head            
            # prev.next = None
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        second_half = reverse(slow)
        # print(second_half)
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        return True

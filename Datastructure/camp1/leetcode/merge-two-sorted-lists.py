# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        else:
            _min = min(list1.val,list2.val)
            if _min == list1.val:
                return ListNode(_min,self.mergeTwoLists(list1.next,list2))
            else:
                return ListNode(_min,self.mergeTwoLists(list1,list2.next))    
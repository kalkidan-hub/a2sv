# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if l1 and not l2:
            res = l1
            while l1.next:

                r = l1.val//10
                l1.val = l1.val % 10
                l1 = l1.next
                if l1:
                    l1.val += r
            r = l1.val//10
            l1.val = l1.val % 10
            if r:
                l1.next = ListNode(r)
            return res
        if l2 and not l1:
            res = l2
            while l2.next:

                r = l2.val//10
                l2.val = l2.val % 10
                l2 = l2.next
                if l2:
                    l2.val += r
            r = l2.val//10
            l2.val = l2.val % 10
            if r:
                l2.next = ListNode(r)
            return res

        v = (l1.val + l2.val) % 10
        r = (l1.val + l2.val)//10

        r_node = None
        if r and l1.next:
            l1.next.val += r
        elif r and l2.next:
            l2.next.val += r
        elif r:
            r_node = ListNode(r)



        curr_node = ListNode(v,self.addTwoNumbers(l1.next,l2.next))
        if r_node:
            curr_node.next = r_node

        return curr_node

        
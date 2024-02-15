# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size,curr = 0, head

        while curr:
            size += 1
            curr = curr.next
        answer = []
        curr = head
        if k >= size:
            while curr:
                tmp = curr.next
                curr.next = None
                answer.append(curr)
                curr = tmp
                k -= 1
            while k:
                answer.append(None)
                k -= 1
        else:
            sub_size = size/k
            prv = curr
            if sub_size > size//k:
                # first operation    
                for _ in range(size%k):
                    s = math.ceil(sub_size)
                    curr = prv
                    while s-1:
                        curr = curr.next
                        s -= 1
                    tmp = curr.next
                    curr.next = None

                    answer.append(prv)
                    prv = tmp
            
            
            while prv:
                s = int(sub_size)
                curr = prv
                while s-1:
                    curr = curr.next
                    s -= 1
                tmp = curr.next
                curr.next = None

                answer.append(prv)
                prv = tmp
        
        return answer     
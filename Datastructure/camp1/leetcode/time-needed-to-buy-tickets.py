class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # optimized way
        res = 0
        for i in range(len(tickets)):
            res += min(tickets[i],tickets[k] - (i > k))
        return res
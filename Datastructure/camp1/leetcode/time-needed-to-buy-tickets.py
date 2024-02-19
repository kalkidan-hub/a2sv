class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # simulating the process
        # worst case the loop runs 100*100 times
        res = 0
        while tickets[k]:
            for i in range(len(tickets)):
                if tickets[i]:
                    tickets[i] -= 1
                    res += 1
                if i == k and tickets[i] == 0:
                    break

        return res
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = [0]*(max(costs)+1)
        
        for cost in costs:
            count[cost] += 1
    
        # s_coins = []
        # for v in range(len(count)):
        #     if count[v]:
        #         s_coins += [v]*count[v]

        buy = 0
        for pr,ct in enumerate(count):
            if pr == 0:
                continue
            if pr > coins or coins <= 0:
                break
            buy +=  min(ct,coins//pr)
            coins -= (pr*ct)           
        
        
        # for p in s_coins:
        #     if p <= coins:
        #         buy += 1
        #         coins -= p
        #     else:
        #         break


        return buy

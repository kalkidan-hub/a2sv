class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles,reverse = True)
        coins = 0
        for i in range(1,len(piles) - len(piles)//3,2):
            coins += piles[i]
        return coins
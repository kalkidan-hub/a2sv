class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # minimize sum of the window of size len(cardPoints) - k
        # calculate the maximum score by substracting the result from the total sum

        wind_size = len(cardPoints) - k
        _sum = sum(cardPoints[:wind_size])
        min_sum = _sum

        for i in range(len(cardPoints)-wind_size):
            _sum = _sum - cardPoints[i] + cardPoints[i+wind_size]
            min_sum = min(min_sum,_sum)
        
        return sum(cardPoints) - min_sum

class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        total = sum([int(b) for b in s])

        zero = 0
        one = 0

        for b in range(len(s) - 1):

            if int(s[b]):
                one += 1
            else:
                zero += 1
            score = max(score, zero + total - one)

        return score
        
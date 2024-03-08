class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # meta data in action
        if k == 1:
            return 0
        boundary_sum = []
        for i in range(1,len(weights)):
            boundary_sum.append(weights[i-1] + weights[i])
        boundary_sum.sort()
        return sum(boundary_sum[-(k-1):]) - sum(boundary_sum[:(k-1)])
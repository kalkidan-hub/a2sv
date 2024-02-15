class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0
        while maxDoubles and target > 1:
            # if target is odd 
            if target & 1:
                steps += 1
            target //= 2
            steps += 1
            maxDoubles -= 1
        if target > 1:
            steps += (target - 1)

        return steps
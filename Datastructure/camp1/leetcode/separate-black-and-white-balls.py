class Solution:
    def minimumSteps(self, s: str) -> int:
        # the zeros afterwards need to pass at least over all the ones before them to get to the front

        steps = 0
        zeros = 0
        for j in range(len(s)-1,-1,-1):
            if s[j] == '0':
                zeros += 1
            else:
                steps += zeros
        return steps
class Solution:
    def numberOfWays(self, s: str) -> int:
        # for each index calculate number of ones and zeros we have both before and after it, 

        _sum = sum([int(st) for st in s])
        running_sum = 0

        answer = 0

        # if the value of s at the current index is zero, consider number of ones before and after it
        # if the value of s at the current index is one, consider the number of zeros before and after it
    
        for i in range(len(s)):

            ones_before = running_sum
            ones_after = _sum - running_sum - int(s[i])

            if int(s[i]):
                # we want zeros before and after current index
                # zeros before, i - running sum
                zeros_before = i - running_sum
                # zeros after, len(s) - i - 1 - ones_after
                zeros_after = (len(s) - i - 1) - ones_after
                answer += zeros_before * zeros_after
            else:
                # we want ones before and after the current index
                answer += ones_before * ones_after

            running_sum += int(s[i])
        
        return answer
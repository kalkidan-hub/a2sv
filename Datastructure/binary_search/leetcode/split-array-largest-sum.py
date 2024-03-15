
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # lets take our boundaries be when we devided our array into len(nums) splits, and into one split
        # and make our search thereafter, 
        def checker(max_sum):
            splits, curr = 1, 0
            act_max = 0
            for v in nums:
                if curr + v > max_sum:
                    splits += 1
                    #act_max = max(act_max,curr)
                    curr = v
                else:
                    curr += v
            #act_max = max(act_max,curr)
            return splits
        
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            splits = checker(mid)
            #print(splits,act_max)
            if splits > k:
                left = mid + 1
            else:
        
                right = mid - 1
                
        return left
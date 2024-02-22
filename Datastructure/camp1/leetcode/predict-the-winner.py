class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # possible_scores = []
        def score(start,end,flag,_sum):
            nonlocal nums
            if start > end:
                return _sum >= 0
            if flag:
                # flag = not flag
                choice1 = score(start,end-1,not flag,_sum + nums[end])
                choice2 = score(start + 1, end,not flag, _sum + nums[start])

                return choice1 or choice2
            else:
                # flag = not flag
                choice1 = score(start,end-1,not flag,_sum - nums[end])
                choice2 = score(start + 1, end,not flag, _sum - nums[start])

                return choice1 and choice2

        
        return score(0,len(nums) - 1,True,0)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        enum = [(val,i) for i,val in enumerate(nums)]

        enum.sort()
        l,r = 0, len(nums)-1
        while l < r:
            if enum[l][0] + enum[r][0] > target:
                r -= 1
            elif enum[l][0] + enum[r][0] < target:
                l += 1
            else:
                return [enum[l][1],enum[r][1]]

        
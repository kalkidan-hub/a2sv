class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ls=[]
        for i in range(1,(len(nums)+1)):
            ls+=[sum(nums[:i])]
        return ls
            
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        triangles = 0
        for i in range(len(nums)-1,1,-1):
            hypoth = nums[i]
            # performing two sum, while our target being hypoth,
            j, k = i-1, 0
            while k < j:
                if nums[j] + nums[k] > hypoth:
                    triangles += j - k
                    j -= 1
                else:
                    k += 1
            
                
        return triangles
                    


        
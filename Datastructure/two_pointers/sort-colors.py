class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # selection sort, 
        '''
        w = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                nums[w],nums[r] = nums[r],nums[w]
                w += 1

        w = len(nums)-1
        for r in range(len(nums)-1,-1,-1):
            if nums[r] == 2:
                nums[w],nums[r] = nums[r],nums[w]
                w -= 1
        '''
        # Dutch national flag problem, algorithm of Dijkstra
        # merging the previous two loops in one
        i,j = 0,0
        k = len(nums)-1

        while j <= k:
            if nums[j] == 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[k],nums[j] = nums[j],nums[k]
                k -= 1
            else:
                j += 1
        

            
                
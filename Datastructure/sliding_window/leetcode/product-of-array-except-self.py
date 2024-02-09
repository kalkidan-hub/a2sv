class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiplication of the numbers previous to it and numbers afterward to it, 
        
        pre = [1]
        post = [1]
        
        for i in range(len(nums) - 1):
            pre.append(pre[-1] * nums[i])
        
        for j in range(len(nums) - 1, 0,-1):
            post.append(post[-1] * nums[j])
            
            
        post = post[::-1]  
        
        return [pr * pos for pr,pos in zip(pre,post)]
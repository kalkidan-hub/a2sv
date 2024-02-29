# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        # findinig maximum index
        
        max_index = 0
        for i in range(len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i
        
        if max_index == len(nums) - 1:
            return TreeNode(nums[max_index],self.constructMaximumBinaryTree(nums[:max_index]), None)
        elif max_index == 0:
            return TreeNode(nums[max_index],None, self.constructMaximumBinaryTree(nums[max_index + 1:]))
        return TreeNode(nums[max_index],self.constructMaximumBinaryTree(nums[:max_index]), self.constructMaximumBinaryTree(nums[max_index + 1:]))
            

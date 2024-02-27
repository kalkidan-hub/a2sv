# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checker(root,_min,_max):    
            if not root:
                return True
            if not(_min < root.val < _max):
                return False
            else:
                return checker(root.left,_min,min(_max,root.val)) and checker(root.right,max(_min,root.val),_max)
        
        return checker(root,-inf,inf)
    
         
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def maxSumBST(self, root) -> int:
        res = 0
        def solve(root):
            nonlocal res
            if not root:
                # mx,mn,valid,act_sum   
                return -inf, inf,1,0
            
            lmx,lmn,lvalid,lsum = solve(root.left)
            rmx,rmn,rvalid,rsum = solve(root.right)

            if lvalid and rvalid and root.val > lmx and root.val < rmn:

                curr_sum = lsum + rsum + root.val
                res = max(res,curr_sum)
                return max(rmx,root.val),min(lmn,root.val), 1,curr_sum
            else:
                return 0,0,0,0
                
        solve(root)    
        return res
        
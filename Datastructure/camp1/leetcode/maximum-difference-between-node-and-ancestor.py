# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # exhaustive search
        def helper(root,ancestors = []):
            if not root:
                return 0
            my_max = 0
            for anc in ancestors:
                my_max = max(my_max,abs(anc.val - root.val))
            ancestors.append(root)
            left_max = helper(root.left,ancestors)
            while ancestors[-1] != root:
                ancestors.pop()
            right_max = helper(root.right,ancestors)

            return max(my_max,left_max,right_max)
        
        return helper(root)

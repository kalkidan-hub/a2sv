# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def helper(root,curr,ans):
            if not root:
                return 0
            curr += str(root.val)
            if not root.right and not root.left:
                ans += int(curr)
                return ans

            left = helper(root.left,curr,ans)
            right = helper(root.right,curr,ans)

            return left + right

        return helper(root,"",0)
        
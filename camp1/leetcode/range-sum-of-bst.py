# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        def traverse(root):
            nonlocal result,low,high
            if not root:
                return 
            if low <= root.val <= high:
                result += root.val
            if root.val <= low:
                traverse(root.right)
            elif root.val >= high:
                traverse(root.left)
            else:
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return result
        
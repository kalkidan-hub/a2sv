# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        left, right = root.left, root.right

        def symmetry(r1,r2):

            if not r1 and not r2:
                return True
            elif( r1 and not r2) or (not r1 and r2):
                return False
            else:
                side = symmetry(r1.left,r2.right)
                middle = symmetry(r1.right,r2.left)
                return r1.val == r2.val and side and middle

        return symmetry(left,right)       
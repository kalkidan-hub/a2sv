# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = defaultdict(list)
        level[0] = [1]
        def traverse(root,x,curr):
            if not root:
                return
            if curr:
                level[x].append(int(curr,2))

            traverse(root.left,x + 1,curr + '0')
            traverse(root.right,x + 1,curr + '1')

        traverse(root,0,'')  
        ans = 0
        for l in level:
            lev = level[l]
            ans = max(ans,lev[-1] - lev[0] + 1)

        return ans   
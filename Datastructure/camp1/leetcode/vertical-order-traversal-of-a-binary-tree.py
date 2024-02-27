# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        map = defaultdict(list)
        def helper(root,y,x):
            if not root:
                return 
            map[y].append((root.val,x))

            helper(root.right,y + 1,x + 1)
            helper(root.left,y -1, x + 1)

        helper(root,0,0)
        ans = []
        
        for k in sorted(map):
            ls = map[k]
            ls = sorted(ls,key= lambda x: (x[-1],x[0]))
            ans.append([l[0] for l in ls])
        return ans      
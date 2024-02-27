# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # kinda odd level reverse traversal

        record = defaultdict(list)

        def traverse(root,level):
            if not root:
                return
            record[level].append(root.val)
            traverse(root.left,level + 1)
            traverse(root.right,level + 1)
        traverse(root,0)
        res = []
        for i in record:
            if i%2:
                res.append(record[i][::-1])
            else:
                res.append(record[i])
        return res




        
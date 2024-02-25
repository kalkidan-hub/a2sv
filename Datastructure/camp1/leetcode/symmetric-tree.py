# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        record = []
        def traverse(root,node):
            if not root:
                record.append(node)
                return 
            node += str(root.val)
            if not root.right and not root.left:
                record.append(node)
                return
            traverse(root.right,node)
            traverse(root.left,node)
        traverse(root,'')
        # check the palindromicity, of the record, 
        i, j = 0, len(record) - 1
        return all([record[i+k] == record[j-k] for k in range(len(record)//2)])
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        arr = inorder(root)
        def buildBinTree(arr):
            if not arr:
                return 
            mid = len(arr)//2
            l_arr = arr[:mid]
            r_arr = arr[mid + 1:]
            
            root = TreeNode(arr[mid])
            root.left = buildBinTree(l_arr)
            root.right = buildBinTree(r_arr)
            
            return root
        
            
        
        return buildBinTree(arr)
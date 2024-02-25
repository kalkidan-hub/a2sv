# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        def populate_freq(root):
            if not root:
                return
            if root.val in freq:
                freq[root.val] += 1
            else:
                freq[root.val] = 1
            populate_freq(root.right)
            populate_freq(root.left)
            
        populate_freq(root)
        print(freq)
        res = []
        _max = 0
        for i in freq:
            if freq[i] == _max:
                res.append(i)
            if freq[i] > _max:
                res = []
                res.append(i)
                _max = freq[i]
        return res
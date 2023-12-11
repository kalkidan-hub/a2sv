class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        val_idx = {nums[i]:i for i in range(len(nums))}

        for op in operations:
            
            idx = val_idx[op[0]]
            nums[idx] = op[1]
            val_idx.pop(op[0])
            val_idx[op[1]] = idx
            
        return nums
        
        
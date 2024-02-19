class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_map = {}
        mono_stack = []

        # monotonicity construction
        for n in nums2:
            while mono_stack and mono_stack[-1] < n:
                v = mono_stack.pop()
                next_greater_map[v] = n
            mono_stack.append(n)
        
        # result accumulation
        result = []
        for n1 in nums1:
            if n1 in next_greater_map:
                result.append(next_greater_map[n1])
            else:
                result.append(-1)

        return result
        
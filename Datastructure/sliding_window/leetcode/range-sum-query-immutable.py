class NumArray:

    def __init__(self, nums: List[int]):
        self.prf_sum = [0]
        for n in nums:
            self.prf_sum.append(self.prf_sum[-1] + n)        

    def sumRange(self, left: int, right: int) -> int:
        return self.prf_sum[right+1] - self.prf_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
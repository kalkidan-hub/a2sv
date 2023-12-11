class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        initial = sum(filter(lambda num: num%2 == 0,nums))
        res = []

        for q in queries:
            val,idx = q[0],q[1]
            if nums[idx] % 2 and val % 2:
                initial += nums[idx] + val
            elif not nums[idx] % 2 and val % 2:
                initial -= nums[idx]
            elif not nums[idx] % 2 and not val % 2:
                initial += val
            res.append(initial)
            nums[idx] += val

        return res
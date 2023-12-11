class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ct_pro = Counter(arr)

        for n in ct_pro:
            if ct_pro[n]/len(arr) > 0.25:
                return n
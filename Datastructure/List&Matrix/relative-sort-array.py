class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        weight = {val:idx for idx,val in enumerate(arr2)}
        for ar in arr1:
            if ar not in weight:
                weight[ar] = 1000 + ar
        return sorted(arr1, key=lambda val: weight[val])



       
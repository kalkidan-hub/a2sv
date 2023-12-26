class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        _map = {heights[i]:names[i] for i in range(len(names))}
        heights.sort()
        return [_map[hei] for hei in heights[::-1]]
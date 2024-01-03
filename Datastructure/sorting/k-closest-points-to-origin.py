class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points,key=lambda a:(a[0]**2 + a[1]**2)**0.5)[:k]
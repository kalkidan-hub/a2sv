class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        # print(points)
        answer = 1
        family = points[0][1]

        for p in points:
            if p[0] <= family:
                continue
            
            answer += 1
            family = p[1]

        return answer    
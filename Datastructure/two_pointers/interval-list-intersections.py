class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1,p2 = 0,0
        intersection = []

        while p1 < len(firstList) and p2 < len(secondList):
            if firstList[p1][1] < secondList[p2][0]:
                p1 += 1
            elif firstList[p1][0] > secondList[p2][1]:
                p2 += 1
            else:
                intersect = [max(firstList[p1][0],secondList[p2][0]),min(firstList[p1][1],secondList[p2][1])]
                intersection.append(intersect)
                
                m = min(firstList[p1][1],secondList[p2][1])
                if m == firstList[p1][1] and m == secondList[p2][1]:
                    p1 += 1
                    p2 += 1
                elif m == firstList[p1][1]:
                    p1 += 1
                else:
                    p2 += 1
                 
        
        return intersection
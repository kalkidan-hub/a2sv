class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = [0] + self.getRow(rowIndex - 1) + [0]
        curr = []
        for i in range(1,len(prev)):
            curr.append(prev[i-1] + prev[i])
        return curr
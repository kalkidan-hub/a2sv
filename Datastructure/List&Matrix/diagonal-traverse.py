class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # brute simulation,
        m,n = len(mat),len(mat[0])

        def valid(coord):
            nonlocal n,m
            return 0 <= coord[0] < m and 0 <= coord[1] < n

        res = []
        curr = (0,0)

        # simulating going up
        def up(curr):
            nonlocal res

            while valid(curr):
                res.append(mat[curr[0]][curr[1]])
                curr = curr[0] - 1, curr[1] + 1
            curr = curr[0] + 1, curr[1] - 1 
            return (curr[0],curr[1] + 1) if valid((curr[0],curr[1] + 1)) else (curr[0] + 1,curr[1])
        # simulating going down
        def down(curr):
            nonlocal res

            while valid(curr):
                res.append(mat[curr[0]][curr[1]])
                curr = curr[0] + 1, curr[1] - 1
            curr = curr[0] - 1, curr[1] + 1   
            return (curr[0] + 1,curr[1]) if valid((curr[0] + 1,curr[1])) else (curr[0],curr[1] + 1)
        
        while curr != (m-1,n-1):
            for move in [up,down]:
                curr = move(curr)
                if curr == (m-1,n-1):
                    break

        res.append(mat[curr[0]][curr[1]])

        return res
             
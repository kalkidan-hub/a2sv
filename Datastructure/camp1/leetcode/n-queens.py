class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        curr = []
        possible_arrangements = []

        def generate_attack_area(i,j):
            attack_areas = []
            for r in range(1,n + 1):
                attack_areas.append((r,j))
                attack_areas.append((i,r))
            x, y = i, j
            while 0 < x <= n and 0 < y <= n:
                attack_areas.append((x,y))
                x -= 1
                y -= 1
            x, y = i, j
            while 0 < x <= n and 0 < y <= n:
                attack_areas.append((x,y))
                x -= 1
                y += 1
            x, y = i, j
            while 0 < x <= n and 0 < y <= n:
                attack_areas.append((x,y))
                x += 1
                y += 1
            x, y = i, j
            while 0 < x <= n and 0 < y <= n:
                attack_areas.append((x,y))
                x += 1
                y -= 1
            return set(attack_areas)


        def backtrack(q):
            
            if q == n + 1:
                possible_arrangements.append(curr.copy())
                return 
                
            for col in range(1,n + 1):

                watch = generate_attack_area(q,col)
                if not watch.intersection(set(curr)): # if not under watch
                    curr.append((q,col))
                    backtrack(q + 1)
                    curr.pop()

        backtrack(1)
        result = []
        for res in possible_arrangements:
            row_arr = []
            for val in res:
                row = ""
                for i in range(1,n + 1):
                    if i == val[1]:
                        row += 'Q'
                    else:
                        row += '.'
                row_arr.append(row)
            result.append(row_arr)

        return result        
        
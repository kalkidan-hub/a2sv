class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        init = m * n
        obstacles = set([tuple(g) for g in guards])
        obstacles.update([tuple(w) for w in walls])
        seen = set()

        for x,y in guards:
            cupi, cupj = x-1,y
            cdowi, cdowj = x+1,y
            cli,clj = x,y-1
            cri,crj = x,y+1

            while (cupi,cupj) not in obstacles and cupi >= 0:
                seen.add((cupi,cupj))
                cupi -= 1
            while (cdowi,cdowj) not in obstacles and cdowi < m:
                seen.add((cdowi,cdowj))
                cdowi += 1
            while (cli,clj) not in obstacles and clj >= 0:
                seen.add((cli,clj))
                clj -= 1
            while (cri,crj) not in obstacles and crj < n:
                seen.add((cri,crj))
                crj += 1
        
        return init - len(obstacles) - len(seen)

        
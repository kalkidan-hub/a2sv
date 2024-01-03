class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        skill_sum = skill[0] + skill[-1]
        chemistry = skill[0]*skill[-1]

        i,j = 1,len(skill) - 2
        while i < j:
            if skill[i] + skill[j] != skill_sum:
                return -1
            chemistry += skill[i]*skill[j]
            i += 1
            j -= 1
        
        return chemistry
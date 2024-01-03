class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        i, j = 0, len(people)-1
        while i < j:
            s = people[i] + people[j]
            if s > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            boat += 1
        return boat + 1 if i == j else boat



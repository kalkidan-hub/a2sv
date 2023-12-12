class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        front = defaultdict(set)
        back = defaultdict(set)

        for i in range(len(fronts)):
            front[fronts[i]].add(i)
        for i in range(len(backs)):
            back[backs[i]].add(i)
        
        good = inf
        for card in front:
            if card not in back or not(front[card].intersection(back[card])):
                good = min(good,card)
        for card in back:
            if card not in front or not(back[card].intersection(front[card])):
                good = min(good,card)
        
        return good if good != inf else 0


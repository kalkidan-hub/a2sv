class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        index_record = {}
        pick = len(cards)

        for i,c in enumerate(cards):
            if c in index_record:
                pick = min(pick,i-index_record[c])
            index_record[c] = i

        return pick + 1 if pick != len(cards) else -1
        
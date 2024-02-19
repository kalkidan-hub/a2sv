class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # reverse simulation
        # start from the final desired output, 
        deck = sorted(deck)
        res = deque() # since we will be doing the appending operation in the front of the list...

        while deck:
            if res:
                # put what's at the bottom at the top, 
                # to reverse, 
                # If there are still cards in the deck then put the next top card of the deck at the bottom of the deck
                res.appendleft(res.pop())
            # append the next lesser card part of the deck, to reverse, 
            # Take the top card of the deck, reveal it, and take it out of the deck
            res.appendleft(deck.pop())

        return res       
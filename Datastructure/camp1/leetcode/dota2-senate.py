class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # reconnaissance

        R, D = [], []
        for i in range(len(senate)):
            if senate[i] == 'R':
                R.append(i)
            else:
                D.append(i)

        # simulate the process using queue
        R, D = deque(R),deque(D)
        while R and D:
            if R[0] < D[0]:
                D.popleft()
                v = R.popleft()
                R.append(v + len(senate))
            else:
                R.popleft()
                v = D.popleft()
                D.append(v + len(senate))

        if R:
            return "Radiant"
        else:
            return "Dire"        
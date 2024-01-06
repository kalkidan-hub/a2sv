class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
        
        n_ct = Counter(name)
        t_ct = Counter(typed)

        # check freq
        if all(t in n_ct and t_ct[t] >= n_ct[t] for t in t_ct):
            # check sequence
            n_seq = [[name[0],1]]
            t_seq = [[typed[0],1]]
            for n in name:
                if n_seq[-1][0] != n:
                    n_seq.append([n,1])
                else:
                    n_seq[-1][1] += 1
            
            for t in typed:
                if t_seq[-1][0] != t:
                    t_seq.append([t,1])
                else:
                    t_seq[-1][1] += 1

            if len(n_seq) == len(t_seq):
                return all(n_seq[i][1] <= t_seq[i][1] and n_seq[i][0] == t_seq[i][0] for i in range(len(n_seq)))


            

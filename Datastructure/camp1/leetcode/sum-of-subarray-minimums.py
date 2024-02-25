class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        # to simplify operation, 
        arr.append(0)
        arr = [0] + arr
        mono_stack = [] 
        mp = defaultdict(list)

        for i,elem in enumerate(arr):
            if i >= 1:
                lst = mono_stack[-1]
                while lst[1] > elem:        
                    mp[lst[0]].append(i - lst[0])
                    mono_stack.pop()
                    lst = mono_stack[-1]
                mp[i].append(i - lst[0])
            mono_stack.append((i,elem))
        # print(mp) 
        ans = 0 
        for idx in range(1, len(arr) - 1):
            ans += arr[idx] * mp[idx][0] * mp[idx][1]

        return ans % MOD
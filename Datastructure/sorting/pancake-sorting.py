class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        end = len(arr)
        for i in range(len(arr)):
            # find the max
            m = arr.index(max(arr[:end]))
            ans.append(m+1)
            ans.append(end)


            arr[:m+1] = arr[:m + 1][::-1]
            arr = arr[:end][::-1]

            end -= 1

        return ans




        
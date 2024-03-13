class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def bin_search(l,r):
            if l > r:
                return l
            mid = (l + r)//2
            if letters[mid] == target:
                return mid
            if letters[mid] > target:
                return bin_search(l,mid - 1)
            else:
                return bin_search(mid + 1,r)
        
        v = bin_search(0,len(letters) - 1)
        if v == -1:
            return letters[0]
        while v < len(letters) and letters[v] == target:
            v += 1
        return letters[v] if v < len(letters) else letters[0]
      
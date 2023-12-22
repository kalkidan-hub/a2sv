class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = 0
        for i in range(len(arr)-1):
            if i == 0 and arr[i] >= arr[i+1]:
                break
            if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
                peak = i
                break

        if peak:
            # check dec
            for j in range(peak,len(arr) - 1):
                if arr[j] <= arr[j + 1]:
                    return False
            return True 
        



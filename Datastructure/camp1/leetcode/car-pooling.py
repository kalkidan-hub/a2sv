class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # the maximum distance the car travelled
        max_dis = 0
        for t in trips:
            max_dis = max(max_dis,t[2])

        # prepare an array of size max_distance
        arr = [0]*(max_dis + 2)

        for t in trips:
            arr[t[1]] += t[0]
            arr[t[2]] -= t[0]
        # calculate prefix sum

        prf_sum = [0]

        for c in arr:
            prf_sum.append(prf_sum[-1] + c)
        
        return all([passenger <= capacity for passenger in prf_sum])

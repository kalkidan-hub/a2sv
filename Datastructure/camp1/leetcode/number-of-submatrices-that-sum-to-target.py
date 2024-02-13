class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # a function to operate on the 1D array

        total = 0
        def oneD_version(arr):
            nonlocal target, total
            hashset = {0:1}
            prf_sum = 0

            for num in arr:
                prf_sum += num
                key = prf_sum - target

                if  key in hashset:
                    total += hashset[key]
                
                if prf_sum in hashset:
                    hashset[prf_sum] += 1
                else:
                    hashset[prf_sum] = 1
                    
        # constructing the modified marix
        m,n = len(matrix[0]), len(matrix)
        modified_matrix = []
        for row in range(n):
            prf = [0]
            for col in range(m):
                prf.append(prf[-1] + matrix[row][col])
            modified_matrix.append(prf)
        
        # print(modified_matrix)
        for c1 in range(1,m+1):
            for c2 in range(c1,m+1):
                arr = [0]*n
                for i in range(n):
                    arr[i] = modified_matrix[i][c2] - modified_matrix[i][c1-1]
                oneD_version(arr)
        
        return total
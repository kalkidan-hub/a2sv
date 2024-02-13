class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        # traverse through the array to constract a minute arrays 
        # such that each minute array contains indexes of the same value

        hashset = defaultdict(list)
        for idx,num in enumerate(nums):
            hashset[num].append(idx)

        # prepare the answer array

        answer = [0]*len(nums)

        for val in hashset:
            minut_array = hashset[val]
            total = sum(minut_array)
            prf_sum = 0

            for i,idx in enumerate(minut_array):

                answer[idx] += (idx*i - prf_sum) + (total - prf_sum) - idx*(len(minut_array) - i)
                prf_sum += idx


        return answer
        
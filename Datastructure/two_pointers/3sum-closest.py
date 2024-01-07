class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = inf
        nums.sort()
        for i in range(len(nums)):
            n_target = target - nums[i]
            near_up,near_down = None,None
            l,r = 0,len(nums)-1

            while l < r:
                if l == i:
                    l += 1
                if r == i:
                    r -= 1
                if l < r:
                    s = nums[l] + nums[r]

                    if s > n_target:
                        near_up = s
                        r -= 1
                    elif s < n_target:
                        near_down = s
                        l += 1
                    else:
                        near_up = near_down = s
                        break
            
            if near_up == None:
                dist = abs(target - (nums[i] + near_down))
                closest = nums[i] + near_down if dist <= abs(target - closest) else closest
            elif near_down == None:
                dist = abs(target - (nums[i] + near_up))
                closest = nums[i] + near_up if dist <= abs(target - closest) else closest
            else:
                d1 = abs(target - (nums[i] + near_down))
                d2 = abs(target - (nums[i] + near_up))
                d3 = abs(target - closest)
                d = min(d1,d2,d3)
                if d == d1:
                    closest = nums[i] + near_down
                elif d == d2:
                    closest = nums[i] + near_up
            # print(closest)


        return closest
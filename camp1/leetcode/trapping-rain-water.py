class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [height[0]]
        right_max = [height[-1]]

        for i in range(1,len(height)):
            left_max.append(max(left_max[-1],height[i]))
        for j in range(len(height) - 2,-1,-1):
            right_max.append(max(right_max[-1],height[j]))
        right_max.reverse()
        water = 0
        for i in range(len(height)):
            trap = min(left_max[i],right_max[i]) - height[i]
            if trap > 0:
                water += trap
        return water
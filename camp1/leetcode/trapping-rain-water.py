class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer approach

        left, right = 0, len(height) - 1
        left_bar, right_bar = height[left], height[right]

        water = 0

        while left < right:
            if left_bar < right_bar:
                if height[left] > left_bar:
                    left_bar = height[left]
                else:
                    water += left_bar - height[left]
                    left += 1
            else:
                if height[right] > right_bar:
                    right_bar = height[right]

                else:
                    water += right_bar - height[right]
                    right -= 1
        return water
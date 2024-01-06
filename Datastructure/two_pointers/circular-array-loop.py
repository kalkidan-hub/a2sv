class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # exhaustive search
        for i in range(len(nums)):
            s = set()
            # sign management,
            back = nums[i] < 0
            forward = nums[i] > 0
            move,prev_move = i,i
            move_dir = True

            while move not in s:
                s.add(move)
                prev_move = move
                move = (nums[move] + move)%len(nums)

                if back:
                    move_dir = move_dir and nums[move] < 0
                else:
                    move_dir = move_dir and nums[move] > 0

            if move != prev_move and move_dir:
                return True

        return False
            


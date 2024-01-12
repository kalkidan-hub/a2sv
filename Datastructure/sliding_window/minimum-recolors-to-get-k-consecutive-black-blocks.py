class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        first_window = blocks[:k].count('W')
        min_operation = first_window
        for i in range(len(blocks)-k):
            curr_window = first_window - (blocks[i] == 'W') + (blocks[i+k] == 'W')
            min_operation = min(min_operation,curr_window)
            first_window = curr_window
        return min_operation
        
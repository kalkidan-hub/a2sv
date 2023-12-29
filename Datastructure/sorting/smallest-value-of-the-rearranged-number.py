class Solution:
    def smallestNumber(self, num: int) -> int:
        num_str = [n for n in str(abs(num))]
        
        num_str.sort(reverse=num < 0)
        if num > 0:
            for i in range(len(num_str)):
                if num_str[i] != '0':
                    num_str[i],num_str[0] = num_str[0],num_str[i]
                    break

        res = int("".join(num_str))
        return res if num >= 0 else -1*res 
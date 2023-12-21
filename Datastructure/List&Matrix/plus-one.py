class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry,dig = 1,len(digits)-1
        
        while dig >= 0 and carry:
            num = carry + digits[dig]
            digits[dig] = (num % 10)
            carry = num//10
            dig -= 1
        
        return [1] + digits if carry else digits


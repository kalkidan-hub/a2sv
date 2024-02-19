class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','/','*']
        for t in tokens:
            if t in operators:
                operand1 = (stack.pop())
                operand2 = (stack.pop())
                if t == '+':
                    res = operand2 + operand1
                elif t == '-':
                    res = operand2 - operand1
                elif t == '/':
                    res = int(operand2 / operand1)
                elif t == '*':
                    res = operand2 * operand1
                
                stack.append(res)
            else:
                stack.append(int(t))
        
        return stack[0]
                
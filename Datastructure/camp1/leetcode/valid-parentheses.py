class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')','{':'}','[':']'}
        stack = []
        for p in s:
            if p in pairs.keys():
                stack.append(p)
            else:
                if stack:
                    top = stack.pop()
                    if pairs[top] != p:
                        return False
                else:
                    return False
        return len(stack) == 0
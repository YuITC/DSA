# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            '(' :   ')',
            '{' :   '}',
            '[' :   ']'
            }

        stack = []
        for x in s:
            if x in dict: stack.append(x)
            else:
                if len(stack) == 0 or x != dict[stack[-1]]: return False
                else: stack.pop()
        
        return len(stack) == 0

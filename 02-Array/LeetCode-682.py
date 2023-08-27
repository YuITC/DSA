# 682. Baseball Game
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for S in operations:
            if S == "C":
                stack.pop()
            elif S == "D":
                stack.append(stack[-1]*2)
            elif S == "+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(S))
        return sum(stack)

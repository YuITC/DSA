# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f1, f2 = 0, 1
        for i in range(n):
            f1, f2 = f2, f1 + f2
        return f2

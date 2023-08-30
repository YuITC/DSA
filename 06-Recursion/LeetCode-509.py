# 509. Fibonacci Number
class Solution:
    def fib(self, n: int) -> int:
        f0, f1 = 0, 1
        for i in range(n):
            f0, f1 = f1, f0 + f1
        return f0
"""    
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
"""

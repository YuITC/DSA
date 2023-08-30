# 225. Implement Stack using Queues
from collections import deque
class MyStack:

    def __init__(self):
        self.Q = deque()

    def push(self, x: int) -> None:
        self.Q.append(x)

    def pop(self) -> int:
        top_ele = self.Q.pop()
        return top_ele

    def top(self) -> int:
        return self.Q[-1]

    def empty(self) -> bool:
        return len(self.Q) == 0

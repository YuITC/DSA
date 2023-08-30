# 1700. Number of Students Unable to Eat Lunch
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dict = {
                1: students.count(1), 
                0: students.count(0) }

        for i in sandwiches:
            if dict[i]: dict[i] -= 1
            else: break
        return sum(dict.values())

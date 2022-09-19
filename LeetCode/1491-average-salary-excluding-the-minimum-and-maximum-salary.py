class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()

        divisor = len(salary) - 2  # exclude min, max

        if len(salary) == 3:
            answer = salary[1]
        else:
            answer = sum(salary[1:-1]) / divisor
        
        return answer

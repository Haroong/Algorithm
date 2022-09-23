class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        
        for idx, value in enumerate(nums):
            if idx == 0:
                sum = value
            else:
                sum = answer[idx - 1] + value
                
            answer.append(sum)

        return answer

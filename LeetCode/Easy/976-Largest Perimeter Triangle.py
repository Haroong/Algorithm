class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        for a, b, c in zip(nums, nums[1:], nums[2:]):
            if a < b + c:
                answer = a + b + c
                return answer
        
        return 0
        

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cnt = 0
        
        # check negative number
        for n in nums:
            if n < 0:
                cnt += 1
            elif n == 0:
                return 0
            else:
                continue
            
        # check negative count
        if cnt % 2 == 1:
            return -1
        else:
            return 1

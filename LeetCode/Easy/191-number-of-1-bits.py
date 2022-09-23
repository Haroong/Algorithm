class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        
        while n:
            if n & 1 == 1: # compare with 1
                answer += 1
            
            n = n >> 1 # move 1 bit
            
        return answer

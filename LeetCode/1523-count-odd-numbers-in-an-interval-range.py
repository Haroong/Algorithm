class Solution:
    def countOdds(self, low: int, high: int) -> int:
        totNum = high - low + 1
        
        if totNum % 2 == 0: # count low to high: even number
            answer = totNum // 2
        else:
            if low % 2 == 1: # starts with odd number
                answer = totNum // 2 + totNum % 2
            else:
                answer = totNum // 2
                
        return answer

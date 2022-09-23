class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        step = arr[1] - arr[0]
        
        for idx in range(1, len(arr)):
            if arr[idx] - arr[idx-1] != step:
                return False
            
        return True

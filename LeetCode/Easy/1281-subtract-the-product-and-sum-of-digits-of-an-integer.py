class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0 # product, sum
        number = list(map(int, str(n)))
        
        for n in number:
            p *= n
            s += n
        
        return p - s

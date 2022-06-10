class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if n < 0:
            inverse = True
        else: 
            inverse = False
            
        n = abs(n)
        out = 1        
        while n > 0:
            i=1
            res = x
            while 2*i < n:
                res = res*res
                i = i*2
            n = n - i
            out = out*res
        
        if inverse:
            return 1/out
        else:
            return out
        
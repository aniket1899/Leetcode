class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        uglies = [2, 3 , 5]
        uglies = [(u, n % u) for u in [2, 3 , 5]]
        
        for u, d in uglies:
            if d == 0:
                while n%u == 0:
                    n = n//u
        return n == 1
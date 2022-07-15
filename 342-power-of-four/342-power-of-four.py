class Solution:
    def powFour(self, n):
        if n == 1:
            return True
        if n % 4:
            return False
        return self.powFour(n//4)
        
            
        
    def isPowerOfFour(self, n: int) -> bool:
        # if n <= 1:
        #     return n == 1
        
        # print(binary)
        ## Method #1: 
        # binary = list(reversed(bin(n)[2:]))
        # return n>0 and binary.count('1') == 1 and binary.index('1') % 2 == 0
        
        ## Method #2: 
        # binary = list(reversed(bin(n)[2:]))
        # return n>0 and n & (n-1) == 0 and binary.index('1') % 2 == 0        
        
        ## Method #3:
        if n <= 0:
            return False
        
        return self.powFour(n)
        
        
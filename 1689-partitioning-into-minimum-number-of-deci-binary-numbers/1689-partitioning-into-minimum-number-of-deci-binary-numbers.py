import re
class Solution:
    # def isBinary(self, n):
        
    def minPartitions(self, n: str) -> int:
        # count = 0
        # while int(n):
        #     sub = re.sub(r"[^0]", "1", n)
        #     n = str(int(n) - int(sub))
        #     count +=1 
        # return count
                          
        return max(n)
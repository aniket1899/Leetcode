from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ctr = Counter(s)
        
        for idx, ch in enumerate(s):
            if ctr[ch] == 1:
                return idx
            
        return -1
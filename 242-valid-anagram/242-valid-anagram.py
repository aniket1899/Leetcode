class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lens = len(s)
        lent = len(t)
        
        if lens != lent:
            return False
        counts = {}
        for i in range(lens):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1
            if t[i] in counts:
                counts[t[i]] -= 1
            else:
                counts[t[i]] = -1
        # print(counts.values())
        # return not any(counts.values())
        for c in counts.values():
            if c!=0:
                return False
        return True
                
            
        
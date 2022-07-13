from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        smap = defaultdict(lambda: None)
        for i in range(len(s)):
            if smap[s[i]]:
                if smap[s[i]] != t[i]:
                    return False
            else:
                smap[s[i]] = t[i]
                    
        return True
        
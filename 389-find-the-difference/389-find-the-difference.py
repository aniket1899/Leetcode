class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        skip = 0
        for i, ch in enumerate(s):
            if ch != t[i]:
                return t[i]
                
        return t[-1]   
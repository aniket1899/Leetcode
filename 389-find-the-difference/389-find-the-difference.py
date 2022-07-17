from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        ctrS = Counter(s)
        ctrT = Counter(t)
        
        for key, val in ctrT.items():
            if key not in ctrS or val == ctrS[key] + 1:
                return key
        
#         s = sorted(s)
#         t = sorted(t)
#         skip = 0
#         for i, ch in enumerate(s):
#             if ch != t[i]:
#                 return t[i]
                
#         return t[-1]   

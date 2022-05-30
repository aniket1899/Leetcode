class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        
        lnee = len(needle)
        for i in range(len(haystack) - lnee + 1):
            if needle == haystack[i:i+lnee]:
                return i
            
        return -1
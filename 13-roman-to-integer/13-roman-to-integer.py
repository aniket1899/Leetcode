class Solution:
    def romanToInt(self, s: str) -> int:
        
        i = 0
        N = len(s)
        roman = {   'I':1,
                    'V': 5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000
        }
        num = 0
        while i<N:
            if i+1 < N and roman[s[i]] < roman[s[i+1]]:
                num += roman[s[i+1]]-roman[s[i]]
                i+=2
            else:
                num += roman[s[i]]
                i+=1
        
        return num
                
                
            
            
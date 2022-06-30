class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        sign = 1
        
        N = len(s)
        i = 0
        while i < N:
            if s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] in '*/':
                sign = 1
                stk.append(s[i])
            elif s[i] != ' ':
                start = i
                while i < N and s[i] not in '+-*/ ':
                    i+=1
                num = float(s[start:i])
                i-=1
                if stk and str(stk[-1]) in '*/':
                    op = stk.pop()
                    if op == '*':
                        lastNum = stk.pop()
                        stk.append(int(lastNum*(sign*num)))
                    elif op == '/':
                        lastNum = stk.pop()
                        stk.append(int(lastNum/(sign*num)))
                else:
                    stk.append(int(sign*num))
            
            i+= 1
   
        return int(sum(stk))
                        
                    
                
                
                
                